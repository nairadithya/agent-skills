# Figure examples

Paths are relative to the skill directory. Reference scripts write PNG and PDF files to their adjacent `figures/` directories and can be run from any working directory. Requires NumPy and Matplotlib. Data files are local; use the user's data for their figures.

| Need | Script | Output in adjacent `figures/` |
|---|---|---|
| Bar, trend and heatmap basics | `examples.py` | `figures/examples.png` and `.pdf` in the working directory |
| Stacked composition by prompt and domain | `references/figure_Brainteaser/plot_brute_force_readable.py` | `brute_force` (math), `brute_force_logic` |
| Annotated categorical heatmaps | `references/figure_Brainteaser/plot_subcategory_readable.py` | `correctness_by_category`, `correctness_by_subcategory`, `selfcorrection_math`, and their separate logic or human-error figures |
| Method comparison with computed spread | `references/figure_CellSpliceNet/plot_comparison_readable.py` | `comparison_human`, `comparison_worm`; mean ± population SD across three supplied values |
| Multi-metric estimates and comparisons | `references/figure_Cflows/plot_readable.py` | `fig2_comparison_GeneRegulatory`, `fig2_comparison_Trajectory`, `figX_comparison_Ablation` |
| Method comparison and ablation | `references/figure_ImmunoStruct/plot_readable.py` | `bars_comparison_IEDB`, `bars_comparison_Cancer`, `bars_ablation_IEDB` (dot-and-interval plots) |
| Benchmark comparison | `references/figure_VIGIL/plot_comparison_readable.py` | `comparison_benchmark`; benchmark panels use different score scales |

Cflows and ImmunoStruct intervals preserve the supplied error magnitudes, but their statistical meanings are not established here. Do not use these examples to infer an uncertainty definition. For reusable patterns see `references/PATTERNS.md`; for design checks see `references/DESIGN.md`.
