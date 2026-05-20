# PreserveAspectRatio — Axis Detection Investigation
*Session date: 2026-05-17*

---

## Summary

During code review of the `PreserveAspectRatio` feature (commit `7685a4f`), we investigated whether
`_applyAspectRatio` in `CurvedArray.py` correctly identifies the primary axis for non-axis-aligned
base shapes. We found a real bug: the tie-breaking behavior of `axabs.index(max(axabs))` silently
produces wrong geometry when the array axis is diagonal (e.g., a sketch on a 45°-rotated datum plane).
The fix — a guard that detects ambiguous axes and emits a warning instead of silently misbehaving —
was added at `CurvedArray.py:178`.

---

## The Original Concern

`_applyAspectRatio` (lines 177–178 at time of investigation) used:

```python
axabs = [abs(ax.x), abs(ax.y), abs(ax.z)]
primary = axabs.index(max(axabs))
```

`list.index()` returns the **first** occurrence of the maximum. If two or more components are equal
(e.g., axis = `(0.707, 0, 0.707)`), the method picks index 0 (X) by accident. This misidentifies
the primary axis, causing the wrong scale factor to be used and the wrong cross-section axis to be
adjusted — silently wrong output, no error.

---

## FreeCAD Placement Axis vs. Plane Normal

A key question was whether `obj.Axis` could ever be diagonal in normal workflow, or only through
manual user entry.

FreeCAD's sketch `Placement.Rotation` stores a rotation as axis + angle. The **rotation axis** is
what the Properties panel displays, and it is **not** the same as the plane normal:

| Sketch plane | Plane normal | Placement rotation axis |
|---|---|---|
| XY | `(0, 0, 1)` | `(0, 0, 1)` (zero-rotation convention) |
| XZ | `(0, 1, 0)` | `(1, 0, 0)` — 90° around X |
| YZ | `(1, 0, 0)` | `(0.577, 0.577, 0.577)` — 120° around `(1,1,1)/√3` |

The YZ plane uses the 120° rotation (instead of 90° around Y) because it simultaneously orients the
plane normal to `(1,0,0)` **and** keeps the sketch's local "up" aligned with world Z. A 90°-around-Y
rotation would leave "up" pointing at world Y (sideways from the user's perspective).

**The `(0.577, 0.577, 0.577)` value is purely a UI artifact and never flows into `obj.Axis`.**

---

## How `getNormal()` Works

`CurvedShapes.getNormal()` (`CurvedShapes.py:282`) is called by `execute()` to auto-set `obj.Axis`
when the user has not specified one:

```python
def getNormal(obj):
    if hasattr(obj, 'Dir'):
        return obj.Dir
    else:
        bbox = obj.Shape.BoundBox
        if bbox.XLength < epsilon: return Vector(1.0,0.0,0.0)
        elif bbox.YLength < epsilon: return Vector(0.0,1.0,0.0)
        elif bbox.ZLength < epsilon: return Vector(0.0,0.0,1.0)
        return obj.Placement.Rotation.multVec(Vector(0, 0, 1))
```

For sketches on a base plane, the flat-dimension check catches it and returns a clean axis-aligned
vector. The placement rotation axis is never used in this path.

### Verified results (sketches with geometry)

```
xy sketch:  getNormal=Vector (0.0, 0.0, 1.0)   placement rotation axis=Vector (0.0, 0.0, 1.0)
xz sketch:  getNormal=Vector (0.0, 1.0, 0.0)   placement rotation axis=Vector (1.0, 0.0, 0.0)
yz sketch:  getNormal=Vector (1.0, 0.0, 0.0)   placement rotation axis=Vector (0.577, 0.577, 0.577)
```

### Watch out: empty sketches

Empty sketches have zero extent in all dimensions. `bbox.XLength < epsilon` fires first for all
three, so all return `(1,0,0)` regardless of plane. Not a bug for CurvedArray (a base with no
geometry is useless anyway), but worth knowing if you ever call `getNormal()` diagnostically.

---

## The Non-Base-Plane Case

For objects not on a base plane — sketches on datum planes, sketches attached to angled faces,
Part objects that have been rotated — none of the three flat-dimension checks in `getNormal()` fire.
It falls through to:

```python
return obj.Placement.Rotation.multVec(Vector(0, 0, 1))
```

This can return any vector. A 45°-around-Y datum plane sketch returns:

```
around y 45:  getNormal=Vector (0.707, 0.0, 0.707)   placement rotation axis=Vector (0.0, 1.0, 0.0)
```

**This is a normal FreeCAD workflow — no manual Axis entry needed.** The diagonal axis flows
directly into `obj.Axis` via auto-detection.

---

## Why Lines 177–178 Cannot Simply Be Removed

The primary/cross_axes decomposition is load-bearing. Without excluding the travel direction:

- For Z-axis array with XZ hull curve: `doScaleXYZsum = [True, False, True]`
- If we don't exclude Z as primary, `constrained = [0, 2]` (X and Z both included)
- `bbox.ZLength` at any slice position is near zero (the intersection is a point on the curve)
- `bbox.ZLength / base.ZLength ≈ 0`, which drags the average scale factor toward zero → wrong result

The exclusion separates "this axis is True because the hull curve spans the travel direction" from
"this axis is True because it constrains cross-section width." That distinction is necessary.

---

## The Fix

The fundamental problem with diagonal axes is architectural: `scaleByBoundbox` operates in world
coordinate axes, so when the travel direction has components in two world axes simultaneously, there
is no clean separation of cross-section from travel. Silent wrong output is worse than a warning.

**Guard added at `CurvedArray.py:178`:**

```python
axabs = [abs(ax.x), abs(ax.y), abs(ax.z)]
sorted_abs = sorted(axabs, reverse=True)
if sorted_abs[0] - sorted_abs[1] < 0.1:
    FreeCAD.Console.PrintWarning(translate("Curved Shapes",
        "PreserveAspectRatio: Axis is not clearly aligned with a coordinate axis — aspect ratio adjustment skipped.\n"))
    return bbox, doScaleXYZ
primary = axabs.index(max(axabs))
cross_axes = [i for i in range(3) if i != primary]
```

**Threshold rationale:** The difference `sorted_abs[0] - sorted_abs[1]` is 0 at exactly 45°
(both components = 0.707) and 1.0 for a perfectly axis-aligned vector. A threshold of 0.1 means
the axis must be within ~42° of a coordinate axis for aspect ratio adjustment to proceed. Cases
closer to 45° than that get a warning and fall back to default (non-aspect-ratio) scaling —
explicit, user-visible, no silent wrong geometry.

---

## Testing Notes

The existing testing checklist in `PreserveAspectRatio-feature.md` covers the axis-aligned cases.
Add:

- [ ] Base shape on a 45°-around-Y datum plane + `PreserveAspectRatio=True` → warning printed,
      output matches `PreserveAspectRatio=False` (falls back to default scaling)
- [ ] Base shape at ~30° tilt (clearly dominant axis, difference > 0.1) → no warning, aspect
      ratio correctly preserved
