"""
chai_style.py — Chai Intellectual house chart style.

Drop this file into every analysis repo. At the top of any notebook:

    from chai_style import apply_style, PALETTE, title, source, save
    apply_style()

Then build charts normally. Call save(fig, "chart-name") to export
a Substack-ready PNG into charts/.

Written once, reused across every Data Dig post. The point is that
readers start recognising her charts before they read the byline.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path

# --- Brand palette -----------------------------------------------------
# Warm neutrals to match the "chai" identity, with a terracotta/slate
# contrast pair chosen to stay distinguishable under red-green colour
# blindness (the most common form).

CREAM      = "#F5EFE6"   # background
ESPRESSO   = "#3B2A20"   # text, axes, primary series
TERRACOTTA = "#C1663A"   # accent 1 — warm
SLATE      = "#2E5C7A"   # accent 2 — cool, safe contrast against terracotta
TAN        = "#8B6F47"   # accent 3
MUTED      = "#A89684"   # gridlines, de-emphasised series

PALETTE = [ESPRESSO, TERRACOTTA, SLATE, TAN, MUTED]


def apply_style():
    """Apply the house style to all subsequent matplotlib figures."""
    mpl.rcParams.update({
        # Canvas
        "figure.facecolor":  CREAM,
        "axes.facecolor":    CREAM,
        "savefig.facecolor": CREAM,
        "figure.figsize":    (9, 5),
        "figure.dpi":        110,

        # Type — serif to match Substack's body font
        "font.family":       "serif",
        "font.serif":        ["Georgia", "Charter", "DejaVu Serif"],
        "font.size":         11,
        "axes.titlesize":    14,
        "axes.titleweight":  "bold",
        "axes.labelsize":    11,

        # Colour
        "text.color":        ESPRESSO,
        "axes.labelcolor":   ESPRESSO,
        "xtick.color":       ESPRESSO,
        "ytick.color":       ESPRESSO,
        "axes.prop_cycle":   mpl.cycler(color=PALETTE),

        # Chrome — strip everything that isn't information
        "axes.spines.top":   False,
        "axes.spines.right": False,
        "axes.spines.left":  False,
        "axes.edgecolor":    MUTED,
        "axes.grid":         True,
        "axes.axisbelow":    True,
        "grid.color":        MUTED,
        "grid.alpha":        0.3,
        "grid.linewidth":    0.6,
        "xtick.bottom":      True,
        "ytick.left":        False,

        # Legend
        "legend.frameon":    False,
        "legend.fontsize":   10,

        "lines.linewidth":   2.2,
    })


def _style_axes(ax):
    """Force house styling onto one Axes, ignoring whatever rcParams say."""
    ax.set_facecolor(CREAM)
    ax.set_prop_cycle(color=PALETTE)

    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.spines["bottom"].set_linewidth(0.8)

    ax.grid(True, color=MUTED, alpha=0.3, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.tick_params(left=False, bottom=True, colors=ESPRESSO, labelsize=10)

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontfamily("serif")
    return ax


def new_fig(nrows=1, ncols=1, figsize=(9, 5), **kwargs):
    """
    Create a styled figure. USE THIS INSTEAD OF plt.subplots().

        fig, ax = new_fig()

    Jupyter's inline backend re-applies its own settings on every figure,
    which silently overrides rcParams. This applies the house style
    directly to the figure and axes objects, so it can't be overridden.
    """
    apply_style()
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize, **kwargs)
    fig.patch.set_facecolor(CREAM)

    try:
        for ax in axes.flat:
            _style_axes(ax)
    except AttributeError:      # single Axes, not an array
        _style_axes(axes)

    return fig, axes


def title(ax, headline, subhead=None):
    """
    Left-aligned headline + optional subhead, newspaper style.

    Use the headline to state the FINDING, not the variable.
      Good:  "Spending rose. Volumes didn't."
      Bad:   "Nominal vs. real spending by category"
    """
    ax.set_title(headline, loc="left", pad=18 if subhead else 10,
                 fontfamily="serif", fontweight="bold",
                 fontsize=14, color=ESPRESSO)
    if subhead:
        ax.text(0, 1.02, subhead, transform=ax.transAxes,
                fontsize=10, color=MUTED, va="bottom",
                fontfamily="serif")


def source(fig, text):
    """Source line, bottom-left. Every chart gets one. No exceptions."""
    fig.text(0.01, 0.01, text, fontsize=8, color=MUTED, ha="left")


def save(fig, name, outdir="charts"):
    """Export a Substack-ready PNG (wide, high-DPI, tight bbox)."""
    Path(outdir).mkdir(exist_ok=True)
    path = Path(outdir) / f"{name}.png"
    fig.savefig(path, dpi=200, bbox_inches="tight",
                facecolor=fig.get_facecolor())
    print(f"saved → {path}")
    return path
