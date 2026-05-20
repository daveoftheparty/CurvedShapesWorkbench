# PreserveAspectRatio Feature — Dev Notes
*Session date: 2026-05-16*

---

## Problem Statement

When using CurvedArray with a circle as the Base and a single hull curve (e.g., in the XZ plane), the circle is stretched along the constrained axis to match the hull curve width, but the other cross-section axis stays at its original size. The result is an ellipse rather than a scaled circle.

**Root cause:** `scaleByBoundbox` (`CurvedShapes.py:143`) scales each axis independently. A hull curve in the XZ plane has no Y extent, so `doScaleXYZsum[1] = False` and `scalevec.y` stays at `1.0` — the original size — while X is scaled to match the hull curve. This is correct behavior for the general case, but loses aspect ratio for symmetric base shapes.

---

## How Hull Curve Scaling Works (Existing Code)

1. **`execute()`** — For each hull curve, inspects its bounding box extents. If a dimension has length > epsilon, that axis is marked as constrained in `doScaleXYZ[n]`. A hull curve in the XZ plane → `doScaleXYZ[n] = [True, False, True]`.

2. **`makeRib()`** — Calls `boundbox_from_intersect()` which intersects the hull curve with a plane at the current position along the array axis. Returns a bounding box populated only on the constrained axes.

3. **`scaleByBoundbox()`** — For each constrained axis: `scalevec[i] = bbox.Length[i] / basebbox.Length[i]`. Unconstrained axes get `scalevec[i] = 1.0`.

---

## Design Decision

**Option A — New command:** Purpose-built command with only Base + single HullCurve. Clean UX, impossible to misuse.
- Rejected: would duplicate all other CurvedArray parameters (Items, Positions, Distribution, Twist, Twists, OffsetStart/End, Surface, Solid, LoftMaxDegree, MaxLoftSize, KeepBase) — large maintenance burden.

**Option B — Boolean on CurvedArray (chosen):** Add `PreserveAspectRatio` property (default `False`). Emit a `PrintWarning` (not a hard error) if enabled with more than one hull curve. Behavior with two hull curves (both axes constrained) is left as-is — user explicitly controls both axes.

---

## Implementation Summary

### Files Changed

#### `CurvedArray.py`

1. **`__init__` signature** — added `PreserveAspectRatio=False` parameter.

2. **Property registration** — added:
   ```python
   CurvedShapes.addObjectProperty(obj, "App::PropertyBool", "PreserveAspectRatio", "CurvedArray",
       QT_TRANSLATE_NOOP("App::Property",
       "Scale the Base shape uniformly based on the single Hullcurve, preserving its aspect ratio. Requires exactly one Hullcurve.")
   ).PreserveAspectRatio = PreserveAspectRatio
   ```

3. **Hullcurves tooltip updated** to mention PreserveAspectRatio:
   > "Bounding curves. Use a single curve with PreserveAspectRatio to scale the Base shape uniformly."

4. **`makeRib()`** — after getting the bbox from `boundbox_from_intersect`, conditionally calls `_applyAspectRatio` before passing to `scaleByBoundbox`:
   ```python
   doScaleXYZ = self.doScaleXYZsum
   if hasattr(obj, 'PreserveAspectRatio') and obj.PreserveAspectRatio and len(obj.Hullcurves) == 1:
       bbox, doScaleXYZ = self._applyAspectRatio(obj, bbox, list(self.doScaleXYZsum))
   return CurvedShapes.scaleByBoundbox(obj.Base.Shape, bbox, doScaleXYZ, copy=True)
   ```

5. **`_applyAspectRatio()` (new method):**
   - Finds the primary axis (most aligned with `obj.Axis`) and the two cross-section axes.
   - Identifies which cross-section axes are constrained by the hull curve and which are not.
   - Computes the scale factor from the constrained axis.
   - Expands the bbox for unconstrained cross-section axes to match that same scale factor, and marks them as needing scaling in `doScaleXYZ`.

6. **`execute()`** — warning if misused:
   ```python
   if hasattr(prop, 'PreserveAspectRatio') and prop.PreserveAspectRatio and len(prop.Hullcurves) != 1:
       FreeCAD.Console.PrintWarning(translate("Curved Shapes",
           "PreserveAspectRatio requires exactly one Hullcurve — ignored.\n"))
   ```

7. **`onChanged()`** — backwards compatibility for older documents:
   ```python
   if not hasattr(fp, 'PreserveAspectRatio'):
       CurvedShapes.addObjectProperty(fp, "App::PropertyBool", "PreserveAspectRatio", "CurvedArray",
           QT_TRANSLATE_NOOP(...), init_val=False)
   ```

#### `CurvedShapes.py`

- **`makeCurvedArray()`** — added `PreserveAspectRatio=False` parameter and passes it through to `CurvedArray.CurvedArray(...)`.



---

## Notes / Known Limitations

- When both cross-section axes are constrained (two hull curves), `_applyAspectRatio` returns early — the existing per-axis scaling takes over unchanged. This is intentional.
- The bbox center for the unconstrained axis is derived from the **base shape's** bounding box center, not the hull curve position. This keeps the shape centered relative to the base.

## Fixed original known limitations

No longer concerns:

- `_applyAspectRatio` uses the **average** scale factor if somehow multiple constrained axes are present (shouldn't happen with a single hull curve, but defensive).
