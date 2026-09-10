"""
Sakura & Rakaposhi — a fractal valley at dusk
================================================

A generative scene combining FOUR distinct fractal / self-similar
construction techniques into one composition, drawing on real visual
motifs from two places:

  Japan (ukiyo-e woodblock aesthetics)
    - indigo / gold dusk palette ("aizome" indigo dye, gold leaf)
    - seigaiha (青海波) — the traditional nested-arc "blue ocean wave"
      textile pattern, built here as literal self-similar nested arcs
    - ensō (円相) — the hand-painted, imperfect Zen circle

  Hunza valley, Gilgit-Baltistan, Pakistan
    - the Karakoram ridgeline (Rakaposhi, "Mother of Mist")
    - the valley's famous spring apricot-blossom light
    - the turquoise glacial river
    - the stepped diamond-lattice geometry of traditional Hunza embroidery

Fractal techniques used, and what each one draws:
  1. 1D midpoint displacement (fractal Brownian terrain) -> mountain ridgelines
  2. Circular midpoint displacement                       -> the ensō circle
  3. L-system-style recursive branching w/ golden-angle
     phyllotaxis clustering                                -> the blossoming tree
  4. Recursive nested-arc & recursive diamond subdivision  -> seigaiha waves
                                                                and embroidery border

Requires: numpy, matplotlib
    pip install numpy matplotlib
"""

import math
import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import LineCollection
from matplotlib.animation import FuncAnimation

RNG = random.Random(7)

# ----------------------------------------------------------------------
# Palette — indigo/gold dusk (ukiyo-e) blended into apricot-blossom warmth
# (Hunza valley in bloom season)
# ----------------------------------------------------------------------
INDIGO_DEEP = (0.043, 0.102, 0.200)   # #0b1a33 — night sky, "aizome" indigo
INDIGO_MID  = (0.118, 0.227, 0.373)   # #1e3a5f — Hokusai wave blue
DUSK_MAUVE  = (0.55, 0.35, 0.42)
APRICOT     = (0.949, 0.580, 0.361)   # #f2935c — Hunza blossom-season dusk
GOLD        = (0.831, 0.686, 0.416)   # #d4af6a — gold leaf
TURQUOISE   = (0.247, 0.722, 0.686)   # #3fb8af — glacial Hunza river
BLOSSOM_PINK  = (0.953, 0.714, 0.769)
BLOSSOM_WHITE = (0.992, 0.953, 0.941)
STONE       = (0.482, 0.42, 0.34)     # weathered fort stone


# ----------------------------------------------------------------------
# 1. Midpoint displacement — fractal terrain (used for the ridgeline)
# ----------------------------------------------------------------------
def fractal_ridge(x0, x1, y0, y1, roughness, iterations, seed=0):
    rng = random.Random(seed)
    pts = [(x0, y0), (x1, y1)]
    for i in range(iterations):
        r = roughness * (0.56 ** i)
        new_pts = []
        for j in range(len(pts) - 1):
            p1, p2 = pts[j], pts[j + 1]
            mx = (p1[0] + p2[0]) / 2
            my = (p1[1] + p2[1]) / 2 + rng.uniform(-r, r)
            new_pts.append(p1)
            new_pts.append((mx, my))
        new_pts.append(pts[-1])
        pts = new_pts
    return pts


def draw_ridge_layer(ax, x_range, base_y, peak_y, color, alpha, roughness, seed, base_line=0):
    pts = fractal_ridge(x_range[0], x_range[1], base_y, base_y, roughness, 9, seed)
    xs = [p[0] for p in pts]
    ys = [max(base_line, base_y + p[1] - base_y + (peak_y - base_y) * 0) for p in pts]
    ys = [p[1] for p in pts]
    poly_xy = [(x_range[0], base_line)] + list(zip(xs, ys)) + [(x_range[1], base_line)]
    ax.add_patch(Polygon(poly_xy, closed=True, facecolor=color, edgecolor="none",
                          alpha=alpha, zorder=2))
    return xs, ys


# ----------------------------------------------------------------------
# 2. Circular midpoint displacement — the ensō (imperfect Zen circle)
# ----------------------------------------------------------------------
def enso_points(cx, cy, r, roughness=0.02, iterations=5, gap=0.35, seed=1):
    rng = random.Random(seed)
    n0 = 10
    angles = list(np.linspace(gap, 2 * math.pi - gap, n0))
    pts = [(cx + r * math.cos(a), cy + r * math.sin(a)) for a in angles]
    for i in range(iterations):
        rr = roughness * r * (0.6 ** i)
        new_pts = []
        for j in range(len(pts) - 1):
            p1, p2 = pts[j], pts[j + 1]
            mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            length = math.hypot(dx, dy) or 1
            nx, ny = -dy / length, dx / length
            off = rng.uniform(-rr, rr)
            new_pts.append(p1)
            new_pts.append((mx + nx * off, my + ny * off))
        new_pts.append(pts[-1])
        pts = new_pts
    return pts


# ----------------------------------------------------------------------
# 3. Recursive branching + golden-angle phyllotaxis — the blossom tree
# ----------------------------------------------------------------------
def build_tree(segments, blossoms, x, y, angle, length, depth, max_depth, rng):
    if depth > max_depth or length < 2.5:
        return
    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)
    segments.append(((x, y), (x2, y2), depth))

    if depth >= max_depth - 3:
        golden_angle = math.radians(137.5)
        for k in range(rng.randint(5, 9)):
            rr = 1.6 + 1.1 * math.sqrt(k)
            a = k * golden_angle + rng.uniform(0, 2 * math.pi)
            blossoms.append((x2 + rr * math.cos(a) * 0.6, y2 + rr * math.sin(a) * 0.6))

    if depth < max_depth:
        for i in range(2 if depth < max_depth - 2 else rng.choice([1, 2])):
            spread = math.radians(rng.uniform(14, 34))
            new_angle = angle + (spread if i == 0 else -spread) + rng.uniform(-0.05, 0.05)
            build_tree(segments, blossoms, x2, y2, new_angle,
                       length * rng.uniform(0.72, 0.82), depth + 1, max_depth, rng)


# ----------------------------------------------------------------------
# 4a. Recursive nested arcs — seigaiha (nested "ocean wave") motif
# ----------------------------------------------------------------------
def draw_seigaiha(ax, x_range, y_base, r0, rows=3, nest=3):
    theta = np.linspace(0, math.pi, 40)
    for row in range(rows):
        y = y_base - row * r0 * 0.78
        offset = r0 if row % 2 else 0
        row_alpha = 0.85 - row * 0.22
        color = GOLD if row % 2 == 0 else TURQUOISE
        x = x_range[0] - offset
        while x < x_range[1] + r0:
            for k in range(nest):
                radius = r0 * (1 - k * 0.26)
                xs = x + radius * np.cos(theta)
                ys = y + radius * np.sin(theta)
                ax.plot(xs, ys, color=color, linewidth=0.9,
                         alpha=row_alpha * (1 - k * 0.18), zorder=5)
            x += 2 * r0


# ----------------------------------------------------------------------
# 4b. Recursive diamond subdivision — Hunza embroidery lattice border
# ----------------------------------------------------------------------
def draw_diamond_fractal(ax, cx, cy, size, depth, color, alpha=0.8, zorder=6):
    pts = [(cx, cy + size), (cx + size, cy), (cx, cy - size), (cx - size, cy)]
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=color,
                          linewidth=0.8, alpha=alpha, zorder=zorder))
    if depth == 0 or size < 2:
        return
    new_size = size * 0.42
    for dx, dy in [(new_size * 1.15, 0), (-new_size * 1.15, 0),
                   (0, new_size * 1.15), (0, -new_size * 1.15)]:
        draw_diamond_fractal(ax, cx + dx, cy + dy, new_size, depth - 1, color,
                              alpha=alpha * 0.75, zorder=zorder)


# ----------------------------------------------------------------------
# Scene assembly
# ----------------------------------------------------------------------
class FractalValley:
    W, H = 300, 190

    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(11, 7))
        self.fig.patch.set_facecolor(INDIGO_DEEP)
        self.ax.set_xlim(0, self.W)
        self.ax.set_ylim(0, self.H)
        self.ax.set_aspect("equal")
        self.ax.axis("off")

        self._draw_sky()
        self._draw_enso()
        self._draw_ridges()
        self._draw_embroidery_border()
        self._draw_fort()
        self._draw_tree()
        self._draw_seigaiha_river()
        self._draw_titles()
        self._init_petals()
        self._init_lanterns()

    # -- sky --------------------------------------------------------
    def _draw_sky(self):
        n = 220
        top = np.array(INDIGO_DEEP)
        mid = np.array(DUSK_MAUVE)
        bottom = np.array(APRICOT)
        g = np.linspace(0, 1, n)
        colors = np.empty((n, 1, 3))
        for i, t in enumerate(g):
            if t < 0.55:
                tt = t / 0.55
                colors[i, 0] = top * (1 - tt) + mid * tt
            else:
                tt = (t - 0.55) / 0.45
                colors[i, 0] = mid * (1 - tt) + bottom * tt
        self.ax.imshow(colors, extent=(0, self.W, 0, self.H), origin="lower",
                        aspect="auto", zorder=0)

    # -- ensō (moon) --------------------------------------------------
    def _draw_enso(self):
        cx, cy, r = 215, 138, 34
        for halo_r, a in [(48, 0.05), (40, 0.09), (34, 0.14)]:
            self.ax.add_patch(plt.Circle((cx, cy), halo_r, color=GOLD, alpha=a, zorder=1))
        pts = enso_points(cx, cy, r, seed=3)
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        self.ax.plot(xs, ys, color=GOLD, linewidth=4.5, alpha=0.85,
                     solid_capstyle="round", zorder=1)

    # -- mountains ----------------------------------------------------
    def _draw_ridges(self):
        draw_ridge_layer(self.ax, (-10, self.W + 10), 78, 78, (0.55, 0.62, 0.72),
                          0.45, 22, seed=11, base_line=0)
        draw_ridge_layer(self.ax, (-10, self.W + 10), 60, 60, INDIGO_MID,
                          0.75, 30, seed=22, base_line=0)
        xs, ys = draw_ridge_layer(self.ax, (-10, self.W + 10), 40, 40, INDIGO_DEEP,
                                   0.95, 36, seed=33, base_line=0)
        # faint snow-caps on the tallest front peaks
        for x, y in zip(xs, ys):
            if y > 85:
                self.ax.plot([x - 3, x, x + 3], [y - 6, y, y - 6],
                             color=BLOSSOM_WHITE, alpha=0.6, linewidth=1.2, zorder=3)

    # -- Hunza embroidery lattice border ------------------------------
    def _draw_embroidery_border(self):
        for i, x in enumerate(range(20, self.W - 10, 40)):
            color = GOLD if i % 2 == 0 else TURQUOISE
            draw_diamond_fractal(self.ax, x, self.H - 9, 8, depth=2, color=color, alpha=0.75)

    # -- fort silhouette (Baltit-Fort inspired, simplified) ------------
    def _draw_fort(self):
        base = [(238, 22), (238, 34), (246, 34), (246, 40), (256, 40),
                (256, 34), (264, 34), (264, 22)]
        self.ax.add_patch(Polygon(base, closed=True, facecolor=STONE,
                                   edgecolor="none", alpha=0.9, zorder=6))
        self.ax.plot([251, 251], [40, 45], color=STONE, linewidth=1.4, zorder=6)

    # -- sakura tree ----------------------------------------------------
    def _draw_tree(self):
        segments, blossoms = [], []
        rng = random.Random(42)
        build_tree(segments, blossoms, 62, 20, math.pi / 2, 30, 0, 8, rng)
        self.blossoms = blossoms

        lines, widths, colors = [], [], []
        for (p1, p2, depth) in segments:
            lines.append([p1, p2])
            widths.append(max(0.6, 4.2 - depth * 0.45))
            fade = depth / 8
            colors.append(((0.25 - 0.1 * fade), 0.16, 0.14, 1))
        lc = LineCollection(lines, linewidths=widths, colors=colors, zorder=7,
                             capstyle="round")
        self.ax.add_collection(lc)

        bx = [b[0] for b in blossoms]
        by = [b[1] for b in blossoms]
        bc = [BLOSSOM_PINK if RNG.random() < 0.6 else BLOSSOM_WHITE for _ in blossoms]
        self.ax.scatter(bx, by, s=14, c=bc, alpha=0.9, zorder=8, linewidths=0)

    # -- seigaiha river -------------------------------------------------
    def _draw_seigaiha_river(self):
        self.ax.add_patch(Polygon([(0, 0), (self.W, 0), (self.W, 18), (0, 18)],
                                   facecolor=INDIGO_DEEP, alpha=0.9, zorder=4))
        draw_seigaiha(self.ax, (0, self.W), 4, r0=13, rows=3, nest=3)

    # -- text -------------------------------------------------------
    def _draw_titles(self):
        self.fig.text(0.06, 0.955, "Sakura & Rakaposhi", fontsize=20,
                       family="serif", color=BLOSSOM_WHITE, weight="medium")
        self.fig.text(0.06, 0.925, "a fractal valley at dusk", fontsize=11,
                       family="serif", style="italic", color=GOLD)
        self.fig.text(
            0.06, 0.038,
            "midpoint-displacement terrain -> Karakoram ridgeline   |   "
            "circular midpoint displacement -> ensō   |   golden-angle branching -> blossoming tree",
            fontsize=7.3, family="monospace", color=(0.75, 0.78, 0.85), alpha=0.85)
        self.fig.text(
            0.06, 0.012,
            "nested recursive arcs -> seigaiha wave   |   diamond recursion -> Hunza embroidery lattice",
            fontsize=7.3, family="monospace", color=(0.75, 0.78, 0.85), alpha=0.85)

    # -- falling petals (animated) -----------------------------------
    def _init_petals(self):
        n = 70
        self.petal_x = np.random.uniform(0, self.W, n)
        self.petal_y = np.random.uniform(20, self.H, n)
        self.petal_speed = np.random.uniform(0.25, 0.7, n)
        self.petal_phase = np.random.uniform(0, 2 * math.pi, n)
        self.petal_sway = np.random.uniform(0.4, 1.4, n)
        colors = np.array([BLOSSOM_PINK if RNG.random() < 0.55 else BLOSSOM_WHITE
                            for _ in range(n)])
        self.petal_scatter = self.ax.scatter(
            self.petal_x, self.petal_y, s=10,
            c=colors, alpha=0.85, zorder=9, linewidths=0)

    def _init_lanterns(self):
        n = 22
        self.lant_x = np.random.uniform(10, self.W - 10, n)
        self.lant_y = np.random.uniform(20, 70, n)
        self.lant_phase = np.random.uniform(0, 2 * math.pi, n)
        self.lantern_scatter = self.ax.scatter(
            self.lant_x, self.lant_y, s=26, c=[GOLD] * n, alpha=0.5, zorder=6, linewidths=0)

    # -- animation tick -----------------------------------------------
    def tick(self, frame):
        t = frame * 0.05
        self.petal_y -= self.petal_speed
        self.petal_x += np.sin(t + self.petal_phase) * self.petal_sway * 0.15
        respawn = self.petal_y < 18
        self.petal_y[respawn] = self.H - 2
        self.petal_x[respawn] = np.random.uniform(0, self.W, respawn.sum())
        self.petal_scatter.set_offsets(np.c_[self.petal_x, self.petal_y])

        alpha = 0.35 + 0.35 * (0.5 + 0.5 * np.sin(t * 1.3 + self.lant_phase))
        rgba = np.tile(np.array(list(GOLD) + [1.0]), (len(alpha), 1))
        rgba[:, 3] = alpha
        self.lantern_scatter.set_facecolor(rgba)
        return self.petal_scatter, self.lantern_scatter

    def run(self):
        self.anim = FuncAnimation(self.fig, self.tick, interval=45,
                                   blit=False, cache_frame_data=False)
        plt.show()

    def save_frame(self, path="fractal_valley.png", dpi=200):
        self.fig.savefig(path, dpi=dpi, facecolor=self.fig.get_facecolor())
        print(f"saved {path}")


if __name__ == "__main__":
    scene = FractalValley()
    scene.run()
