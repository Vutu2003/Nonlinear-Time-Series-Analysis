#!/usr/bin/env python3
"""Create the vector NTSA overview at a native size of 127.0 x 77.61 mm.

Run: python ntsa_framework_overview.py
Requires Matplotlib. Font preference: Times New Roman, then Liberation Serif.
The PDF contains selectable, embedded text and vector boxes/connectors.
Designed for approximately 1.5-column placement; no condensed font or text scaling.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile

# Keep font/cache writes outside the manuscript and user configuration folders.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "ntsa-figure-mpl"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, Rectangle


WIDTH_PT, HEIGHT_PT = 360.0, 220.0
LINE_WIDTH = 0.65


def select_font() -> str:
    for family in ("Times New Roman", "Liberation Serif", "Nimbus Roman", "TeX Gyre Termes"):
        try:
            font_manager.findfont(
                font_manager.FontProperties(family=family, style="normal", stretch="normal"),
                fallback_to_default=False,
            )
            return family
        except ValueError:
            continue
    raise RuntimeError("Install a Times-compatible serif font before generating the figure.")


def build_figure(output: Path) -> None:
    family = select_font()
    plt.rcParams.update({
        "font.family": family,
        "font.stretch": "normal",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "text.color": "black",
        "axes.edgecolor": "black",
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "path.simplify": False,
    })
    fig = plt.figure(figsize=(WIDTH_PT / 72, HEIGHT_PT / 72), dpi=144)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set(xlim=(0, WIDTH_PT), ylim=(0, HEIGHT_PT))
    ax.set_axis_off()
    labels: list[tuple[object, tuple[float, float, float, float] | None]] = []

    def text(x, y, value, size, *, bold=False, baseline=False, bounds=None):
        artist = ax.text(
            x, y, value, fontsize=size, ha="center",
            va="baseline" if baseline else "center",
            fontweight="bold" if bold else "normal",
            fontstyle="normal", fontstretch="normal",
            linespacing=1.12, color="black", zorder=3,
        )
        labels.append((artist, bounds))

    def line(points):
        ax.plot(*zip(*points), color="black", lw=LINE_WIDTH,
                solid_capstyle="butt", solid_joinstyle="miter", zorder=1)

    def arrow(start, end):
        ax.add_patch(FancyArrowPatch(
            start, end, arrowstyle="-|>", mutation_scale=5.2,
            linewidth=LINE_WIDTH, color="black", shrinkA=0, shrinkB=0,
            zorder=2,
        ))

    def box(x, y, width, height, *, primary):
        ax.add_patch(Rectangle(
            (x, y), width, height, facecolor="white", edgecolor="black",
            linewidth=0.75 if primary else 0.55, zorder=0,
        ))
        return (x + 3, y + 2, x + width - 3, y + height - 2)

    # Shared input and reconstruction: no acquisition, QC, or statistics layer.
    text(180, 208, "Ultra-short PPG windows", 11.5, bold=True)
    arrow((180, 200), (180, 194))
    text(180, 186, "Phase-space reconstruction", 10.8)
    arrow((180, 178), (180, 173))
    text(180, 165, "Complementary nonlinear characterization", 10.3)

    # One reconstructed signal feeds three equally weighted dynamical views.
    line(((180, 157), (180, 151)))
    line(((57, 151), (303, 151)))
    methods = (
        (7, "Prediction", "Finite-horizon\nforecastability"),
        (130, "RQA", "Recurrence\norganization"),
        (253, "LLE", "Local trajectory\ndivergence"),
    )
    for left, method, observable in methods:
        center = left + 50
        arrow((center, 151), (center, 137))
        bounds = box(left, 85, 100, 52, primary=True)
        text(center, 121.5, method, 12.5, bold=True, baseline=True, bounds=bounds)
        # Shared baselines and line spacing make the three pillars identical.
        for y, label in zip((105.5, 93.5), observable.splitlines()):
            text(center, y, label, 9.6, baseline=True, bounds=bounds)
        line(((center, 85), (center, 66)))

    # These views serve two parallel questions; PPS is not a fourth descriptor.
    line(((57, 66), (303, 66)))
    purposes = (
        (23, "PPS surrogate testing",
         "Organization beyond tested\nnoisy pseudoperiodic null (RQ1)"),
        (195, "Awake–Drowsy comparison",
         "State-related dynamical\nreorganization (RQ2)"),
    )
    for left, heading, purpose in purposes:
        center = left + 71
        arrow((center, 66), (center, 48))
        bounds = box(left, 6, 142, 42, primary=False)
        text(center, 36.5, heading, 9.8, bold=True, baseline=True, bounds=bounds)
        for y, label in zip((22.5, 11), purpose.splitlines()):
            text(center, y, label, 9.2, baseline=True, bounds=bounds)

    # Catch clipped labels and label overlap before exporting.
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    extents = []
    for artist, bounds in labels:
        extent = artist.get_window_extent(renderer).transformed(ax.transData.inverted())
        permitted = bounds or (2, 2, WIDTH_PT - 2, HEIGHT_PT - 2)
        if not (permitted[0] <= extent.x0 and permitted[1] <= extent.y0
                and extent.x1 <= permitted[2] and extent.y1 <= permitted[3]):
            raise RuntimeError(f"Label outside its intended area: {artist.get_text()}")
        for previous in extents:
            if extent.overlaps(previous):
                raise RuntimeError(f"Overlapping labels near: {artist.get_text()}")
        extents.append(extent)

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, format="pdf", metadata={
        "Title": "Nonlinear dynamical analysis framework for ultra-short PPG",
        "Subject": "Three complementary dynamical views and two research questions",
        "Creator": "Matplotlib; ntsa_framework_overview.py",
        "CreationDate": None,
        "ModDate": None,
    })
    plt.close(fig)
    print(f"Created {output} ({WIDTH_PT:g} x {HEIGHT_PT:g} pt; {family})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".pdf"))
    build_figure(parser.parse_args().output)
