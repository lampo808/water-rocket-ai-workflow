"""Figure docs/figures/fig_inertial_head.png: sensitivity of the apogee
to the inertial head of the water column (eq. W2h).

Reference rocket (code/rocket.py defaults), n = 1.4, gauge pressures
1, 2, 3, 5 bar. Solid: driving pressure p - p_a (W2). Dashed: with the
head rho_w (g + a) h, cylindrical column (W2h). Prints the optimum fill
and apogee of each curve and the relative change.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from rocket import Rocket, simulate

OUT = Path(__file__).resolve().parent.parent / "docs" / "figures" / "fig_inertial_head.png"
INK, MUTED = "#1f1f1e", "#6b6a64"
# Same one-hue ordinal ramp as fig_apogee_vs_fill.py.
COLORS = {1: "#86b6ef", 2: "#3987e5", 3: "#1c5cab", 5: "#0d366b"}

r = Rocket()
fills = np.round(np.arange(0.0, 0.901, 0.01), 3)

fig, ax = plt.subplots(figsize=(6.5, 4.5))
print(f"{'p_g (bar)':>9s} {'head':>5s} {'f_opt':>6s} {'apogee (m)':>11s} {'change':>7s}")
for bar, c in COLORS.items():
    best = {}
    for head, ls in ((False, "-"), (True, "--")):
        h = np.array([simulate(r, fill=f, p_g=bar * 1e5, head=head).apogee
                      for f in fills])
        i = int(np.argmax(h))
        best[head] = h[i]
        change = "" if not head else f"{100 * (h[i] / best[False] - 1):+.1f} %"
        print(f"{bar:9d} {str(head):>5s} {fills[i]:6.2f} {h[i]:11.2f} {change:>7s}")
        ax.plot(fills, h, color=c, lw=2, ls=ls,
                label=f"{bar} bar" if not head else None)
        ax.plot(fills[i], h[i], "o", ms=5, color=c, mec="white", mew=1)
        if not head:
            ax.text(fills[i] + 0.02, h[i], f"{bar} bar", color=INK, fontsize=8,
                    va="top")

ax.plot([], [], color=MUTED, lw=2, ls="-", label="p - p_a (W2)")
ax.plot([], [], color=MUTED, lw=2, ls="--", label="with inertial head (W2h)")
ax.set_xlabel("fill fraction f = V_w0 / V_b")
ax.set_ylabel("apogee (m)")
ax.set_xlim(0, 0.9)
ax.set_ylim(bottom=0)
ax.grid(color="#e4e3dd", lw=0.6)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=8, ncol=2)
ax.set_title("Apogee vs fill fraction: effect of the inertial head, n = 1.4",
             fontsize=10, color=INK)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT.relative_to(OUT.parents[2])}")
