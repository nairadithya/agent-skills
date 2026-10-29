---
name: scientific-figure-making
description: >-
  Publication-ready matplotlib figures for papers, slides, and reports—bars,
  trends, scatter, heatmaps, radar, and multi-panel layouts—using the
  figures4papers house style (minimal spines, semantic blue/green/red palette,
  print-safe encoding, vector export). Use when the user is finalizing or
  creating such figures in matplotlib. Do not use for interactive/web viz
  (Plotly, Altair, Bokeh), exploratory-only plots without a publication target,
  dominant 3D or GIS mapping, or Illustrator/Figma-first infographic workflows.
---

# Scientific figure making

Condensed from [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers)
(CC BY-NC 4.0). The repo's `figure_*` folders are the canonical demos — when a
specific chart type is requested, mirror the closest one.

## House style (apply once per script)

```python
import matplotlib
matplotlib.use("Agg")  # headless/batch; before importing pyplot
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "font.size": 16,              # 24 for large bar panels, 15-16 for compact
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 2.5,        # 3 for big bars, 2 for compact
    "legend.frameon": False,
    "svg.fonttype": "none",       # editable text in vector exports
})
```

## Palette (semantic, keep consistent across panels)

```python
PALETTE = {
    "blue_main": "#0F4D92",      # proposed / key method
    "blue_secondary": "#3775BA",
    "green_1": "#DDF3DE", "green_2": "#AADCA9", "green_3": "#8BCF8B",   # improvements/positives
    "red_1": "#F6CFCB", "red_2": "#E9A6A1", "red_strong": "#B64342",    # baselines/contrasts
    "neutral": "#CFCECE",        # reference/background
    "highlight": "#FFD700",      # single callout only
    "teal": "#42949E", "violet": "#9A4D8E",
}
DEFAULT_COLORS = ["#0F4D92", "#8BCF8B", "#B64342", "#42949E", "#9A4D8E", "#CFCECE"]
```

## Core patterns

- **Ultra-wide panels for multi-metric comparisons:** `figsize=(28, 6)` or
  `(45, 12)` for 3–4 metrics in a row; width ≈ 3–4× height so bars/labels
  don't crowd. One subplot per metric.
- **Dedicated legend panel:** when the legend is large, add an extra subplot,
  `ax.set_axis_off()`, and put the legend there (grab
  `handles, labels = ax.get_legend_handles_labels()` from the first panel).
- **Categorical x-axis without tick labels:** for "method/condition" axes,
  `ax.set_xticks([])` and let the legend/panel title identify series.
- **Error bars:** `capsize=5`, `ecolor='k'` on bars.
- **Tighten y-limits to the data range** (e.g. `data.min()-margin` to
  `data.max()+margin`, or fixed sensible floors like `[0.5, 0.9]`) — never a
  fixed 0–100 that squashes 85–95 values.
- **Print-safe bars:** `edgecolor='black'`, `linewidth>=1.5`; add hatch
  (`'/'`, `'\\'`, `'.'`) for sub-groups so hue-only differences survive grayscale.
- **Ablation ramps:** same color with alpha swept `np.linspace(0.2, 1.0, n)`
  (use `(r, g, b, alpha)` tuples, e.g. `(0.215686, 0.458824, 0.729412, alpha)`)
  to encode "completeness" of the method; annotate exact values above bars
  (`ax.text`, large font) instead of relying on gridlines.
- **Trends:** 2–4 curves per axis, `linewidth=2–3`, `fill_between` for
  uncertainty, minimal/no grid.
- **Radar (polar):** real data vertices only (no interpolation — plot points,
  close the ring), per-axis normalization into a display band (e.g.
  `45 + 45 * clip((v - r_lo) / span, 0, 1)` per benchmark), light
  `axial.fill(..., alpha=0.05)`, per-spoke tick labels.

## Export

- `fig.tight_layout(pad=2)` (pad=1 for compact multi-panel).
- `dpi=300` standard; `dpi=600` for dense bar panels.
- Save both `png` and `pdf` (or svg/eps) under a `figures/` dir —
  `os.makedirs('./figures/', exist_ok=True)`; close with `plt.close(fig)`.
- If venue, dimensions, or export formats are underspecified in a way that
  would change layout or DPI, ask before locking the choice.