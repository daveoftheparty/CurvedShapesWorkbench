# Testing Checklist

## from original feature

- [ ] Circle base + single XZ hull curve (taper) → ribs should remain circular, uniformly scaled
- [ ] Circle base + single XZ hull curve → `PreserveAspectRatio=False` (default) still produces ellipses (no regression)
- [ ] Non-circular base (e.g., rectangle) + single hull curve + `PreserveAspectRatio=True` → uniform scale
- [ ] `PreserveAspectRatio=True` with two hull curves → warning printed, output unchanged from default behavior
- [ ] Existing documents without the property load without error (backwards compat via `onChanged`)
- [ ] `Surface=True` and `Solid=True` modes work correctly with preserved aspect ratio

# from axis investigation
- [ ] Base shape on a 45°-around-Y datum plane + `PreserveAspectRatio=True` → warning printed,
      output matches `PreserveAspectRatio=False` (falls back to default scaling)
- [ ] Base shape at ~30° tilt (clearly dominant axis, difference > 0.1) → no warning, aspect
      ratio correctly preserved
