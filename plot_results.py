from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
root = Path(__file__).resolve().parent
saved = json.loads((root / "findings.json").read_text())
fig, ax = plt.subplots(figsize=(max(8, len(saved["labels"]) * .48), 5.8))
ax.bar(range(len(saved["values"])), saved["values"], color="#3679a0")
ax.axhline(0, color="#333333", linewidth=.8)
ax.set_xticks(range(len(saved["labels"])), saved["labels"], rotation=saved["rotation"], ha="right" if saved["rotation"] else "center")
ax.set_ylabel(saved["unit"])
ax.set_title(saved["title"], loc="left", fontsize=11)
ax.spines[["top", "right"]].set_visible(False)
fig.text(.08, .025, "Reported development aggregates. Conditional assumptions apply. No verified trading edge.", fontsize=8)
fig.tight_layout(rect=(0,.075,1,1))
(root / "figures").mkdir(exist_ok=True)
fig.savefig(root / "figures/testing_results.png", dpi=150)
plt.close(fig)
