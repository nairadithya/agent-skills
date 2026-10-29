---
name: scientific-figure-making
description: >-
  Create or finalize publication-ready matplotlib figures for papers, slides,
  and reports, including bar charts, trends, scatter plots, heatmaps, radar,
  and multi-panel layouts. Not for exploratory-only, interactive/web, 3D,
  GIS, or Illustrator/Figma-first visualization.
---

# Scientific figure making

Use a restrained, print-safe style. Replace illustrative data with the user's data.

- `examples.py`: runnable bar, trend, and heatmap figure.
- `references/PATTERNS.md`: reusable plotting patterns.
- `references/DESIGN.md`: design and review checklist for audience, encoding, captions, and misleading visual choices.
- `references/INDEX.md`: local example scripts and rendered plots, organized by chart type. Read the relevant reference when building a figure; adapt it to the data and final format.

## Workflow

1. Identify the audience, medium, and main message; choose the chart accordingly. Label axes with units and identify methods, conditions, and uncertainty. Do not invent data or imply uncertainty that was not supplied.
2. Size the figure for its final use, not an arbitrarily large canvas. Ask about venue, dimensions, or formats if essential; otherwise state reasonable assumptions.
3. Use consistent colors across panels: blue `#0F4D92` for the primary method, green `#8BCF8B` for positives, red `#B64342` for contrasts, and gray `#CFCECE` for references. Use markers, line styles, or hatches as well as color.
4. Use IBM Plex Sans for labels and legends, IBM Plex Serif for editorial or title text, and IBM Plex Mono for code or fixed-width values. Install the fonts when needed; use suitable fallbacks if unavailable. Remove top/right spines where appropriate, avoid unnecessary gridlines, and keep labels legible at final size. Place a large legend outside the data or in a separate panel.
5. Export a vector PDF or SVG and a 300-dpi PNG unless the user specifies otherwise. Inspect at final size for clipping, readability, and grayscale distinction. Supply or suggest a caption explaining encodings, uncertainty, and transformations; close figures after saving.

## Chart-specific guidance

- **Bars:** start the value axis at zero; use black edges and hatches for print. Show error bars only when defined, and say what they represent. For small differences near a nonzero value, prefer a dot or interval plot over truncated bars.
- **Trends:** use distinct lines/markers and, when available, a labeled uncertainty band. Use data-appropriate limits without hiding relevant variation.
- **Scatter:** label variables and units; use shape as well as color for groups. Avoid connecting unordered observations.
- **Heatmaps:** use a perceptually ordered colormap, a labeled colorbar, and meaningful limits; use a diverging scale centered on zero for signed differences.
- **Radar:** plot actual vertices and close the polygon without interpolation. If axes have different scales, disclose the normalization and show the original units or ranges. Consider a dot plot for precise comparison.
- **Multi-panel:** align comparable axes and preserve shared scales when comparisons require them. Label panels and keep legends consistent.
