"""Directly labeled alternatives for Cflows comparisons and ablations.

Run: python plot_readable.py. Error intervals use supplied magnitudes; their
statistical definition must be checked against the underlying study.
"""
from pathlib import Path
from data import ablation, gene_regulatory, trajectory
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["IBM Plex Sans", "DejaVu Sans"],
                     "font.serif": ["IBM Plex Serif", "DejaVu Serif"], "font.size": 10,
                     "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})


def make(name, labels, panels, xlabels, errors=None, shared=False):
    fig, axes = plt.subplots(1, len(panels), figsize=(3 * len(panels) + 2, max(4, len(labels) * .38)),
                             sharey=True, sharex=shared, layout="constrained", squeeze=False)
    y = np.arange(len(labels))
    for i, ((title, values), ax) in enumerate(zip(panels, axes.flat)):
        error = None if errors is None else errors[i]
        ax.errorbar(values, y, xerr=error, fmt="o", color="#0F4D92", ecolor="#505050", capsize=3, markersize=4)
        ax.set_yticks(y, labels)
        ax.set_title(title, fontfamily="serif", fontsize=10)
        ax.set_xlabel(xlabels[i])
        ax.grid(axis="x", color="#e0e0e0", linewidth=.7)
        ax.set_axisbelow(True)
        ax.tick_params(axis="y", length=0)
    axes.flat[0].invert_yaxis()
    suffix = " — estimates and reported errors" if errors is not None else " — reported means"
    fig.suptitle(name + suffix, fontfamily="serif", fontsize=14)
    for ext in ("png", "pdf"):
        basename = {"Ablation": "figX_comparison_Ablation",
                    "Gene regulatory": "fig2_comparison_GeneRegulatory",
                    "Trajectory": "fig2_comparison_Trajectory"}[name]
        fig.savefig(HERE / "figures" / f"{basename}.{ext}", dpi=300)
    plt.close(fig)


a = ablation
make("Ablation", a["methods"], [(m, a["mean"][m]) for m in a["metrics"]],
     ["Score"] * len(a["metrics"]), [a["std"][m] for m in a["metrics"]])
g = gene_regulatory
make("Gene regulatory", g["methods"], [(d, g["mean"][d]) for d in g["datasets"]],
     [g["metric"]] * len(g["datasets"]), [g["std"][d] for d in g["datasets"]], shared=True)
t = trajectory
labels = [f"{dataset} · {method}" for dataset in t["datasets"] for method in t["methods"]]
panels = [(m, np.concatenate([t["mean"][m][d] for d in t["datasets"]])) for m in t["metrics"]]
make("Trajectory", labels, panels, ["Score"] * len(panels))
