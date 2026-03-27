"""Style showcase — one figure per (style × plot-type) combination.

Covers every registered style and the main night_wave helper functions.
Doubles as a visual test: run it and inspect the saved PNGs.

Usage (from the repo root):
    python examples/style_showcase.py
"""

import os

import numpy as np
from matplotlib import pyplot as plt

import mpl_styler
from mpl_styler.functions import night_wave_func

OUT_DIR = os.path.join(os.path.dirname(__file__), "figures", "showcase")
os.makedirs(OUT_DIR, exist_ok=True)

RNG = np.random.default_rng(42)

STYLES = [
    "sci_pure",
    "sci_faded",
    "night_wave",
    "sci_print",
    "blueprint",
    "minimal",
    "solarized",
    "earth",
]


# ── helpers ────────────────────────────────────────────────────────────────


def _save(name: str) -> None:
    plt.savefig(os.path.join(OUT_DIR, name), bbox_inches="tight")
    plt.close()


# ── 1. Line plot + legend + text box ───────────────────────────────────────


def plot_lines(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, 200)
    for k in range(1, 5):
        ax.plot(x, np.sin(k * x), label=f"$\\sin({k}x)$")

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title(f"{style} — line plot")
    ax.legend(loc="upper right")

    # Text box
    ax.text(
        0.02,
        0.97,
        "Annotation box",
        transform=ax.transAxes,
        va="top",
        bbox=dict(boxstyle="round,pad=0.4"),
    )

    _save(f"{style}_lines.png")


# ── 2. Scatter plot + legend ────────────────────────────────────────────────


def plot_scatter(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    for k in range(4):
        x = RNG.normal(k * 1.5, 0.6, 80)
        y = RNG.normal(k * 0.8, 0.5, 80)
        ax.scatter(x, y, label=f"Group {k + 1}", alpha=0.75)

    ax.set_xlabel("X (a.u.)")
    ax.set_ylabel("Y (a.u.)")
    ax.set_title(f"{style} — scatter")
    ax.legend()

    _save(f"{style}_scatter.png")


# ── 3. Bar chart + error bars + legend + text box ──────────────────────────


def plot_bars(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    categories = ["A", "B", "C", "D", "E"]
    values = RNG.uniform(0.4, 1.0, len(categories))
    errors = RNG.uniform(0.03, 0.12, len(categories))

    ax.bar(categories, values, yerr=errors, capsize=6, label="Measurement")

    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    ax.set_title(f"{style} — bar chart")
    ax.legend()

    ax.text(
        0.98,
        0.97,
        "$n = 100$",
        transform=ax.transAxes,
        ha="right",
        va="top",
        bbox=dict(boxstyle="square,pad=0.3"),
    )

    _save(f"{style}_bars.png")


# ── 4. Histogram (overlapping, alpha) + legend ─────────────────────────────


def plot_histogram(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    for k, label in enumerate(["Sample A", "Sample B", "Sample C"]):
        data = RNG.normal(k * 1.5, 0.8, 400)
        ax.hist(data, bins=30, alpha=0.6, label=label)

    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    ax.set_title(f"{style} — overlapping histograms")
    ax.legend()

    _save(f"{style}_histogram.png")


# ── 5. 2D histogram with colorbar ──────────────────────────────────────────


def plot_hist2d(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    x = RNG.normal(0, 1, 2000)
    y = 0.8 * x + RNG.normal(0, 0.6, 2000)
    h = ax.hist2d(x, y, bins=40)
    fig.colorbar(h[3], ax=ax, label="Count")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"{style} — 2D histogram")

    _save(f"{style}_hist2d.png")


# ── 6. Step plot + fill_between ────────────────────────────────────────────


def plot_fill(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    x = np.linspace(0, 4 * np.pi, 300)
    y1 = np.sin(x)
    y2 = 0.5 * np.sin(2 * x)

    ax.plot(x, y1, label="$\\sin(x)$")
    ax.plot(x, y2, label="$0.5\\sin(2x)$")
    ax.fill_between(x, y1, y2, alpha=0.25, label="Difference")

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title(f"{style} — fill between")
    ax.legend()

    _save(f"{style}_fill.png")


# ── 7. Multi-panel (1×2: lines + bars) ─────────────────────────────────────


def plot_multipanel(style: str) -> None:
    mpl_styler.use(style)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(f"{style} — multi-panel")

    x = np.linspace(0, 4 * np.pi, 300)
    for k in range(3):
        ax1.plot(x, np.cos(x + k * np.pi / 3), label=f"$\\phi={k}\\pi/3$")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$\\cos(x + \\phi)$")
    ax1.set_title("Lines")
    ax1.legend()

    cats = ["P", "Q", "R", "S", "T"]
    values = RNG.uniform(0.2, 1.0, len(cats))
    ax2.bar(cats, values)
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Value")
    ax2.set_title("Bars")

    fig.tight_layout()
    _save(f"{style}_multipanel.png")


# ── 8. Shared-axis subplots ─────────────────────────────────────────────────


def plot_shared_axes(style: str) -> None:
    mpl_styler.use(style)
    fig, axes = plt.subplots(3, 1, sharex=True)
    fig.suptitle(f"{style} — shared x-axis")

    x = np.linspace(0, 2 * np.pi, 200)
    signals = [np.sin(x), np.cos(x), np.sin(x) * np.cos(x)]
    labels = ["$\\sin$", "$\\cos$", "$\\sin\\cdot\\cos$"]

    for ax, sig, lbl in zip(axes, signals, labels):
        ax.plot(x, sig, label=lbl)
        ax.legend(loc="upper right")
        ax.set_ylabel(lbl)

    axes[-1].set_xlabel("$x$")
    fig.tight_layout()
    _save(f"{style}_shared_axes.png")


# ── 9. Log scale + minor ticks ─────────────────────────────────────────────


def plot_logscale(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    x = np.logspace(-1, 3, 200)
    for k, alpha in enumerate([0.5, 1.0, 1.5, 2.0]):
        ax.plot(x, x**alpha, label=f"$x^{{{alpha}}}$")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title(f"{style} — log scale")
    ax.legend()

    _save(f"{style}_logscale.png")


# ── 10. Text-heavy: annotations, arrows ────────────────────────────────────


def plot_annotations(style: str) -> None:
    mpl_styler.use(style)
    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, 200)
    (line,) = ax.plot(x, np.sin(x))

    # Arrow annotation
    ax.annotate(
        "Maximum",
        xy=(np.pi / 2, 1.0),
        xytext=(np.pi / 2 + 0.8, 0.7),
        arrowprops=dict(arrowstyle="->", shrinkB=5),
    )

    # Plain text box
    ax.text(
        3.5,
        -0.6,
        "Plain text box\n$y = \\sin(x)$",
        fontsize=20,
        bbox=dict(boxstyle="round,pad=0.4"),
    )

    # Borderpad/fancybox annotation
    ax.annotate(
        "Minimum",
        xy=(3 * np.pi / 2, -1.0),
        xytext=(3 * np.pi / 2 - 1.2, -0.5),
        arrowprops=dict(arrowstyle="->", shrinkB=5),
        bbox=dict(boxstyle="round,pad=0.3"),
    )

    ax.set_xlabel("$x$")
    ax.set_ylabel("$\\sin(x)$")
    ax.set_title(f"{style} — annotations & text boxes")

    _save(f"{style}_annotations.png")


# ── night_wave extras ───────────────────────────────────────────────────────


def plot_night_wave_line_glow() -> None:
    mpl_styler.use("night_wave")
    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, 200)
    for k in range(1, 5):
        ax.plot(x, np.sin(k * x), label=f"$\\sin({k}x)$")

    night_wave_func.make_lines_glow(ax)

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title("night_wave — line glow")
    ax.legend(loc="upper right")

    _save("night_wave_lines_glow.png")


def plot_night_wave_glow_gradient() -> None:
    mpl_styler.use("night_wave")
    fig, ax = plt.subplots()

    x = np.linspace(0, 2 * np.pi, 200)
    for k in range(1, 4):
        ax.plot(x, np.sin(k * x), label=f"$\\sin({k}x)$")

    night_wave_func.add_glow_and_grad_fill(ax)

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title("night_wave — glow + gradient fill")
    ax.legend(loc="upper right")

    _save("night_wave_lines_glow_grad.png")


def plot_night_wave_bars() -> None:
    mpl_styler.use("night_wave")
    fig, ax = plt.subplots()

    categories = ["A", "B", "C", "D", "E"]
    values = RNG.uniform(0.4, 1.0, len(categories))
    bars = ax.bar(categories, values)
    night_wave_func.add_bar_gradient(bars, ax)

    ax.set_xlabel("Category")
    ax.set_ylabel("Value")
    ax.set_title("night_wave — bar gradient")

    _save("night_wave_bars_grad.png")


def plot_night_wave_hist_gradient() -> None:
    mpl_styler.use("night_wave")
    fig, ax = plt.subplots()

    data = RNG.normal(0, 1, 1000)
    _, _, hist_container = ax.hist(data, bins=30)
    night_wave_func.add_hist_gradient(hist_container, ax)

    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    ax.set_title("night_wave — histogram gradient")

    _save("night_wave_hist_grad.png")


def plot_night_wave_scatter_glow() -> None:
    mpl_styler.use("night_wave")
    fig, ax = plt.subplots()

    x = RNG.normal(0, 1, 150)
    y = RNG.normal(0, 1, 150)
    color_vals = np.hypot(x, y)  # colour by distance from origin
    ax.scatter(x, y, c=color_vals, label="Data", zorder=3)
    night_wave_func.make_scatter_glow(ax)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("night_wave — scatter glow")
    ax.legend()

    _save("night_wave_scatter_glow.png")


# ── main ───────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    plot_funcs = [
        ("line plot", plot_lines),
        ("scatter", plot_scatter),
        ("bar chart", plot_bars),
        ("histogram", plot_histogram),
        ("2D histogram", plot_hist2d),
        ("fill between", plot_fill),
        ("multi-panel", plot_multipanel),
        ("shared axes", plot_shared_axes),
        ("log scale", plot_logscale),
        ("annotations", plot_annotations),
    ]

    for style in STYLES:
        for label, fn in plot_funcs:
            print(f"  {style} — {label}")
            fn(style)

    print("night_wave extras…")
    for label, fn in [
        ("line glow", plot_night_wave_line_glow),
        ("glow + gradient", plot_night_wave_glow_gradient),
        ("bar gradient", plot_night_wave_bars),
        ("hist gradient", plot_night_wave_hist_gradient),
        ("scatter glow", plot_night_wave_scatter_glow),
    ]:
        print(f"  night_wave — {label}")
        fn()

    print(f"\nAll figures saved to: {OUT_DIR}")
