"""Directly labeled comparison of means and population SDs across three values.

Run: python plot_comparison_readable.py
"""
from pathlib import Path
from data import data_comparison
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
data = data_comparison
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["IBM Plex Sans", "DejaVu Sans"],
                     "font.serif": ["IBM Plex Serif", "DejaVu Serif"], "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})


def plot(domain):
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.8), sharey=True, layout="constrained")
    y = np.arange(len(data["methods"]))
    for ax, metric in zip(axes, data["metrics"]):
        values = data[f"result_{domain}"][metric]
        ax.errorbar(values.mean(axis=1), y, xerr=values.std(axis=1), fmt="o",
                    color="#0F4D92", ecolor="#505050", capsize=3, markersize=4, linewidth=1)
        ax.set_yticks(y, data["methods"])
        ax.set_title(metric, fontfamily="serif")
        ax.set_xlabel("Score")
        ax.grid(axis="x", color="#e0e0e0", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.tick_params(axis="y", length=0)
    axes[0].invert_yaxis()
    fig.suptitle(f"{domain.title()} comparison — mean ± population SD (n=3)", fontfamily="serif", fontsize=14)
    for ext in ("png", "pdf"):
        fig.savefig(HERE / "figures" / f"comparison_{domain}.{ext}", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    plot("human")
    plot("worm")
