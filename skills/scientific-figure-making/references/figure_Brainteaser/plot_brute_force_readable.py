"""Readable alternative to the brute-force composition figure.

Run from any directory: python plot_brute_force_readable.py
Writes separate math and logic figures in the local figures directory. Segment values
are the original reported proportions; rounding can make totals differ from 1.
"""
from pathlib import Path
from data import data_brute_force_math, data_brute_force_logic

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.ticker import PercentFormatter

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["IBM Plex Sans", "DejaVu Sans"],
    "font.serif": ["IBM Plex Serif", "DejaVu Serif"],
    "font.monospace": ["IBM Plex Mono", "DejaVu Sans Mono"],
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "legend.frameon": False,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
})

# Outcome, not model, is encoded by fill; method names are labeled directly.
labels = ["Only model", "Only human", "Neither", "Both"]
colors = ["#3775BA", "#E9A6A1", "#E5E5E5", "#8BCF8B"]
hatches = ["//", "\\\\", "", "xx"]


def plot(data, domain):
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.8), layout="constrained", sharex=True)
    for ax, prompt in zip(axes.flat, data["prompts"]):
        values = data["result"][prompt]
        y = np.arange(len(data["methods"]))
        left = np.zeros(len(y))
        for index, (color, hatch) in enumerate(zip(colors, hatches)):
            ax.barh(y, values[:, index], left=left, color=color,
                    edgecolor="black", linewidth=0.6, hatch=hatch, height=0.7)
            left += values[:, index]
        ax.set_yticks(y, data["methods"])
        ax.invert_yaxis()
        ax.set_xlim(0, 1.01)  # Allow for rounding in reported proportions.
        ax.xaxis.set_major_formatter(PercentFormatter(1))
        ax.set_xlabel("Responses")
        ax.set_title(prompt, loc="left", fontfamily="serif")
        ax.tick_params(axis="y", length=0)
    handles = [Patch(facecolor=c, edgecolor="black", hatch=h, label=label)
               for c, h, label in zip(colors, hatches, labels)]
    fig.legend(handles=handles, title="Brute-force outcome", loc="outside lower center", ncols=4)
    fig.suptitle(f"Brute-force outcomes: {domain}", fontfamily="serif", fontsize=15)
    out = HERE / "figures"
    out.mkdir(exist_ok=True)
    for ext in ("png", "pdf"):
        name = "brute_force" if domain == "Math" else "brute_force_logic"
        fig.savefig(out / f"{name}.{ext}", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    plot(data_brute_force_math, "Math")
    plot(data_brute_force_logic, "Logic")
