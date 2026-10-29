# Figure design and review

Use this checklist when designing or revising a figure. A paper figure can rely on a caption; it need not explain the entire study inside the axes.

## Before plotting

- State the audience, medium, and one main message. For a slide, simplify and enlarge; for a paper, keep detail readable at the final print size and explain it in the caption.
- Choose an encoding that supports the comparison: aligned positions for precise comparisons; bars from zero for magnitudes; lines for ordered observations; small multiples when overlapping series are hard to distinguish.
- Identify the data, units, transformations, and uncertainty. Never invent an uncertainty definition or normalize values without saying so.

## Make it readable

- Label series directly when practical; otherwise place a concise legend near the data without covering it. Use consistent names, order, and colors across panels.
- Use a sequential colormap for ordered magnitude, diverging for deviations around a meaningful center, and qualitative colors for categories. Add shape, line style, or hatch where color alone is insufficient. Check grayscale and color-vision accessibility.
- Reduce unnecessary ticks, decimal places, borders, and gridlines, but keep those needed to read values. Avoid low-contrast text on fills or images; annotate only what fits.
- Size markers, line widths, and text for the final physical dimensions. Split a crowded figure rather than relying on an enormous canvas or illegible labels.
- Use data coordinates for data-bound annotations, axes coordinates for panel labels, and point offsets for spacing that should remain stable when limits change.

## Prevent misleading comparisons

- Bars encode magnitude by length: include zero. For narrow differences, use a dot or interval plot with clearly marked limits. Scale scatter marker **area**, not radius, in proportion to quantities.
- Explain non-linear scales, clipping, independent panel scales, and any per-axis normalization. Never imply that line segments, curves, or shaded bands represent observations or uncertainty not present in the data.
- Show the meaning of error bars, bands, and sample sizes in the caption or figure. If unknown, flag it instead of guessing. Captions should identify the comparison, units, encodings, and any transformations needed to interpret it.
- Inspect the exported file at actual presentation size and in grayscale. Check for clipping, overlap, missing fonts, and loss of small marks. When practical, ask someone unfamiliar with the figure what they think it says.
