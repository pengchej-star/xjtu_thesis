from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    default_input = repo_root / "TimeMixer-main" / "results" / "paper_table_full_ablation" / "ablation_wins.csv"
    default_output = repo_root / "image" / "ablation_wins_bar_chart.png"

    parser = argparse.ArgumentParser(description="Generate the ablation win-count bar chart.")
    parser.add_argument("--input", type=Path, default=default_input, help="Path to ablation_wins.csv")
    parser.add_argument("--output", type=Path, default=default_output, help="Output PNG path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.input)

    variants = df["Variant"].tolist()
    x = range(len(variants))
    width = 0.24

    plt.rcParams.update(
        {
            "font.family": "Arial",
            "axes.unicode_minus": False,
            "figure.dpi": 160,
            "savefig.dpi": 300,
        }
    )

    fig, ax = plt.subplots(figsize=(10.5, 5.8))

    bars_mse = ax.bar([i - width for i in x], df["MSEWins"], width, label="MSE wins", color="#3b82f6")
    bars_mae = ax.bar(x, df["MAEWins"], width, label="MAE wins", color="#10b981")
    bars_total = ax.bar([i + width for i in x], df["TotalWins"], width, label="Total wins", color="#f59e0b")

    ax.set_title("Best-count statistics of model variants", fontsize=16, pad=14)
    ax.set_xlabel("Model variant", fontsize=12)
    ax.set_ylabel("Number of best results", fontsize=12)
    ax.set_xticks(list(x), variants)
    ax.set_ylim(0, max(df["TotalWins"]) + 4)
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(ncol=3, frameon=False, loc="upper right")

    for bars in (bars_mse, bars_mae, bars_total):
        ax.bar_label(bars, padding=3, fontsize=9)

    fig.tight_layout()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
