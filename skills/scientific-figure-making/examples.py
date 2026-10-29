"""Runnable style examples with illustrative data; not scientific results.

Run: python examples.py   (requires numpy and matplotlib)
Writes figures/examples.png and figures/examples.pdf in the current directory.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Use a noninteractive backend for batch export.
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["IBM Plex Sans", "DejaVu Sans"],
    "font.serif": ["IBM Plex Serif", "DejaVu Serif"],
    "font.monospace": ["IBM Plex Mono", "DejaVu Sans Mono"],
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 1.2,
    "legend.frameon": False,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
})
BLUE, RED = "#0F4D92", "#B64342"

fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), layout="constrained")

# Bar comparison: error bars represent illustrative standard deviations.
ax = axes[0]
values = [0.72, 0.84]
errors = [0.04, 0.03]
bars = ax.bar(["Baseline", "Proposed"], values, yerr=errors,
              color=[RED, BLUE], edgecolor="black", linewidth=1,
              capsize=4, error_kw={"ecolor": "black"})
bars[0].set_hatch("//")
ax.set_ylim(0, 1)
ax.set_ylabel("Accuracy (fraction)")
ax.set_title("a  Comparison (mean ± SD)", loc="left", fontfamily="serif")

# Trends: the shaded bands represent illustrative 95% confidence intervals.
ax = axes[1]
x = np.arange(1, 6)
for label, y, color, marker, linestyle in [
    ("Baseline", np.array([0.44, 0.53, 0.60, 0.65, 0.68]), RED, "s", "--"),
    ("Proposed", np.array([0.48, 0.61, 0.70, 0.77, 0.82]), BLUE, "o", "-"),
]:
    ax.plot(x, y, label=label, color=color, marker=marker, linestyle=linestyle)
    ax.fill_between(x, y - 0.04, y + 0.04, color=color, alpha=0.15)
ax.set(xlabel="Epoch", ylabel="Accuracy (fraction)", ylim=(0.35, 0.9))
ax.set_title("b  Trends (95% CI)", loc="left", fontfamily="serif")
ax.legend()

# Heatmap: a shared, labeled scale makes comparisons interpretable.
ax = axes[2]
data = np.array([[0.71, 0.76, 0.73], [0.81, 0.84, 0.79]])
image = ax.imshow(data, cmap="viridis", vmin=0, vmax=1, aspect="auto")
ax.set_xticks(range(3), ["A", "B", "C"])
ax.set_yticks(range(2), ["Baseline", "Proposed"])
ax.set_xlabel("Dataset")
ax.set_title("c  Accuracy", loc="left", fontfamily="serif")
for (row, col), value in np.ndenumerate(data):
    ax.text(col, row, f"{value:.2f}", ha="center", va="center", color="black")
fig.colorbar(image, ax=ax, label="Accuracy (fraction)")

out = Path("figures")
out.mkdir(exist_ok=True)
fig.savefig(out / "examples.png", dpi=300)
fig.savefig(out / "examples.pdf")
plt.close(fig)
