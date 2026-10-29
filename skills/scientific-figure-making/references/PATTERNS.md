# Reusable patterns

These are independent snippets, not real results. Each assumes `import numpy as np` and `import matplotlib.pyplot as plt`. Apply the fonts and export settings from `examples.py`. See `references/INDEX.md` for the local example collection.

## Stacked composition

Use `bottom` to accumulate segments; each stack must represent the same total or a clearly labeled count. Use hatches and a legend, not color alone.

```python
fig, ax = plt.subplots(figsize=(4, 3), layout="constrained")
labels = ["Method A", "Method B"]
correct, incorrect = np.array([70, 85]), np.array([30, 15])
ax.bar(labels, correct, label="Correct", color="#0F4D92", edgecolor="black")
ax.bar(labels, incorrect, bottom=correct, label="Incorrect",
       color="#CFCECE", edgecolor="black", hatch="//")
ax.set_ylabel("Responses (count)")
ax.legend()
```

## Radar comparison

Only use with comparable, explicitly normalized metrics. Label original ranges in the caption; do not interpolate between benchmarks. A dot plot is often easier to read.

```python
fig, ax = plt.subplots(figsize=(4, 4), subplot_kw={"projection": "polar"}, layout="constrained")
metrics = ["A", "B", "C", "D"]
angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False)
closed = np.r_[angles, angles[0]]
for label, values, color, marker in [
    ("Baseline", [0.6, 0.8, 0.5, 0.7], "#B64342", "s"),
    ("Proposed", [0.8, 0.7, 0.8, 0.9], "#0F4D92", "o"),
]:
    ax.plot(closed, np.r_[values, values[0]], color=color, marker=marker, label=label)
    ax.fill(closed, np.r_[values, values[0]], color=color, alpha=0.05)
ax.set_xticks(angles, metrics)
ax.set_ylim(0, 1)
ax.set_title("Normalized score (0–1)")
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
```

## Scatter and matrix

For a diffusion-style figure, show observations next to the corresponding matrix; preserve row/column ordering and explain what matrix entries mean. If edges or distances are shown, explain their selection and units.

```python
fig, (ax, matrix_ax) = plt.subplots(1, 2, figsize=(7, 3), layout="constrained")
points = np.array([[0, 0], [1, 1], [2, 0], [3, 1]])
groups = ["A", "A", "B", "B"]
for group, marker, color in [("A", "o", "#0F4D92"), ("B", "s", "#B64342")]:
    mask = np.array(groups) == group
    ax.scatter(points[mask, 0], points[mask, 1], marker=marker, color=color, label=group)
ax.set(xlabel="Coordinate 1 (a.u.)", ylabel="Coordinate 2 (a.u.)")
ax.legend()
distance = np.linalg.norm(points[:, None, :] - points[None, :, :], axis=2)
image = matrix_ax.imshow(distance, cmap="viridis", vmin=0)
matrix_ax.set(xlabel="Observation", ylabel="Observation")
fig.colorbar(image, ax=matrix_ax, label="Distance (a.u.)")
```

## Other constructions

- **Ablation and grouped bars:** offset each group consistently, or use horizontal bars for long labels. Annotate values only when readable. Use zero baselines; switch to dot-and-interval plots when fine differences matter.
- **Sweeps and post-training:** plot ordered parameter values as lines with markers, keep units and reference baselines visible. Explain any gradient encoding and avoid implying interpolated observations.
- **Cumulative trends:** sort timestamps, compute cumulative counts, then use `plot` and optionally `fill_between`; annotate events without covering data. Label cumulative totals, not rates.
- **Annotated heatmaps:** use `imshow` or seaborn, a labeled colorbar, and `ax.text` or `annot=True` when cells are large enough. State whether columns use separate scales.
- **Concepts and 3D surfaces:** use patches, contours, points, or `plot_surface` only when they clarify the mechanism; distinguish schematic geometry from measured data. Label projections and be mindful of occlusion. Use 3D only when it serves the message.
