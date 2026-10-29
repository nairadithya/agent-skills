"""Replace the radar comparison with benchmark-specific dot plots.

Run from any directory: python plot_comparison_readable.py
Values are the reported scores; no per-spoke normalization or imputation.
"""
from pathlib import Path
from data import data_comparison
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
data = data_comparison
plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["IBM Plex Sans", "DejaVu Sans"],
    "font.serif": ["IBM Plex Serif", "DejaVu Serif"],
    "font.monospace": ["IBM Plex Mono", "DejaVu Sans Mono"],
    "font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
    "pdf.fonttype": 42, "svg.fonttype": "none", "legend.frameon": False,
})

fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.3), sharey=True, layout="constrained")
benchmarks = [r"POPE$_{Adv}$", "MathVista", "MMBench"]
models = [key.split("\n")[0] for key in list(data["results"])[:4]]
markers = ["s", "^", "o"]
colors = ["#B64342", "#37804A", "#0F4D92"]
y = np.arange(len(models))
for ax, benchmark in zip(axes, benchmarks):
    scores = np.array([data["results"][model + "\n" + benchmark] for model in models])
    for j, (method, marker, color) in enumerate(zip(data["methods"], markers, colors)):
        ax.scatter(scores[:, j], y + (j - 1) * 0.18, marker=marker,
                   color=color, s=38, label=method, zorder=3)
    ax.set_yticks(y, models)
    ax.set_title(benchmark, fontfamily="serif")
    ax.set_xlabel("Reported score")
    ax.grid(axis="x", color="#dedede", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)
axes[0].invert_yaxis()
handles = [Line2D([], [], marker=m, color=c, linestyle="none", label=label)
           for m, c, label in zip(markers, colors, data["methods"])]
fig.legend(handles=handles, loc="outside lower center", ncols=3)
fig.suptitle("Post-training comparison by benchmark", fontfamily="serif", fontsize=14)
out = HERE / "figures"
for ext in ("png", "pdf"):
    fig.savefig(out / f"comparison_benchmark.{ext}", dpi=300)
plt.close(fig)
