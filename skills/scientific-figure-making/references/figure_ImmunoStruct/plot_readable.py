"""Dot-and-interval alternatives to the comparison and IEDB ablation bars.

Run: python plot_readable.py
Intervals are the original reported error magnitudes, which may differ in
meaning across metrics; consult the underlying study before interpreting them.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from raw_data import data_comparison_IEDB, data_comparison_Cancer, data_ablation_IEDB

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["IBM Plex Sans", "DejaVu Sans"],
    "font.serif": ["IBM Plex Serif", "DejaVu Serif"],
    "font.monospace": ["IBM Plex Mono", "DejaVu Sans Mono"],
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
})


def plot(data, labels, name):
    fig, axes = plt.subplots(1, 3, figsize=(12, max(4.5, len(labels) * 0.38)),
                             sharey=True, layout="constrained")
    y = np.arange(len(labels))
    for i, ax in enumerate(axes):
        ax.errorbar(data["mean"][:, i], y, xerr=data["std"][:, i],
                    fmt="o", color="#0F4D92", ecolor="#505050",
                    capsize=3, markersize=4, linewidth=1)
        ax.set_yticks(y, labels)
        ax.invert_yaxis() if i == 0 else None
        ax.set_title(data["metrics"][i], fontfamily="serif")
        ax.set_xlabel("Score")
        ax.tick_params(axis="y", length=0)
        ax.grid(axis="x", color="#e0e0e0", linewidth=0.7)
        ax.set_axisbelow(True)
    fig.suptitle(name + " — estimates and reported errors", fontfamily="serif", fontsize=14)
    out = HERE / "figures"
    out.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        basename = {"IEDB comparison": "bars_comparison_IEDB",
                    "Cancer comparison": "bars_comparison_Cancer",
                    "IEDB ablation": "bars_ablation_IEDB"}[name]
        fig.savefig(out / f"{basename}.{ext}", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    for dataset, name in [(data_comparison_IEDB, "IEDB comparison"),
                          (data_comparison_Cancer, "Cancer comparison")]:
        labels = [label.replace(r'BigMHC$_\text{retrained}$', 'BigMHC retrained')
                  for label in dataset["methods"]]
        plot(dataset, labels, name)
    components = data_ablation_IEDB["components"]
    labels = [" + ".join(component for bit, component in zip(code, components) if bit == "1")
              for code in data_ablation_IEDB["ablations"]]
    plot(data_ablation_IEDB, labels, "IEDB ablation")
