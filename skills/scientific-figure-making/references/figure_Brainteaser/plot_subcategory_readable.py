"""Annotated heatmaps for subcategory correctness; preserves the reported values.

Run from any directory: python plot_subcategory_readable.py
"""
from pathlib import Path
from data import (category_math, category_logic, subcategory_math,
                  subcategory_logic, selfcorrection_model, selfcorrection_human)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["IBM Plex Sans", "DejaVu Sans"],
    "font.serif": ["IBM Plex Serif", "DejaVu Serif"],
    "font.monospace": ["IBM Plex Mono", "DejaVu Sans Mono"],
    "font.size": 10, "pdf.fonttype": 42, "svg.fonttype": "none",
})


def plot(data, domain, kind="subcategory"):
    names = data["subtypes"]
    values = np.stack([data["result"][name] for name in names])
    fig, ax = plt.subplots(figsize=(10, 2.8 + 0.36 * len(names)), layout="constrained")
    image = ax.imshow(values, cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set_yticks(range(len(names)), names)
    ax.set_xticks(range(len(data["methods"])), data["methods"], rotation=30, ha="right", rotation_mode="anchor")
    ax.tick_params(length=0)
    for (row, col), value in np.ndenumerate(values):
        ax.text(col, row, f"{value:.0%}", ha="center", va="center",
                color="white" if value > 0.55 else "black", fontsize=9)
    title = "Self-correction outcome" if kind == "selfcorrection" else f"Correctness by {kind}"
    ax.set_title(f"{title} — {domain}", fontfamily="serif", loc="left")
    color_label = "Outcome probability" if kind == "selfcorrection" else "Probability correct"
    fig.colorbar(image, ax=ax, label=color_label, shrink=0.7)
    out = HERE / "figures"
    for ext in ("png", "pdf"):
        if kind in ("category", "subcategory"):
            name = f"correctness_by_{kind}"
            if domain == "Logic":
                name += "_logic"
        else:
            name = "selfcorrection_math" if domain == "Model error" else "selfcorrection_math_human_error"
        fig.savefig(out / f"{name}.{ext}", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    plot(subcategory_math, "Math")
    plot(subcategory_logic, "Logic")
    plot(category_math, "Math", "category")
    plot(category_logic, "Logic", "category")
    plot(selfcorrection_model, "Model error", "selfcorrection")
    plot(selfcorrection_human, "Human error", "selfcorrection")
