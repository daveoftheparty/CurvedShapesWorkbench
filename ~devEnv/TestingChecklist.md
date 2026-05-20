# Testing Checklist

## from original feature

- [x] Circle base + single XZ hull curve (taper) → ribs should remain circular, uniformly scaled
- [x] Circle base + single XZ hull curve → `PreserveAspectRatio=False` (default) still produces ellipses (no regression)
- [x] Non-circular base (e.g., rectangle) + single hull curve + `PreserveAspectRatio=True` → uniform scale
- [x] `PreserveAspectRatio=True` with two hull curves → warning printed, output unchanged from default behavior
- [x] Existing documents without the property load without error (backwards compat via `onChanged`)
- [x] `Surface=True` and `Solid=True` modes work correctly with preserved aspect ratio

# from axis investigation
- [x] Base shape on a 45°-around-Y datum plane + `PreserveAspectRatio=True` → warning printed,
      output matches `PreserveAspectRatio=False` (falls back to default scaling)
- [x] Base shape at ~30° tilt (clearly dominant axis, difference > 0.1) → no warning, aspect
      ratio correctly preserved
