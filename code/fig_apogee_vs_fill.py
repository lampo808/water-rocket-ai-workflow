"""Figure docs/figures/fig_apogee_vs_fill.png: apogee vs fill fraction.

Reference rocket (code/rocket.py defaults). Gauge pressures 1, 2, 3,
5 bar. Solid: n = 1.4 (dry adiabat). Dashed: n = 1.2 (lower end of the
exponents measured by Romanelli et al. 2013). Prints the optimum fill
of each curve.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from rocket import Rocket, simulate

OUT = Path(__file__).resolve().parent.parent / "docs" / "figures" / "fig_apogee_vs_fill.png"
INK, MUTED = "#1f1f1e", "#6b6a64"
# One-hue ordinal ramp (light to dark = low to high pressure).
COLORS = {1: "#86b6ef", 2: "#3987e5", 3: "#1c5cab", 5: "#0d366b"}

r = Rocket()
fills = np.round(np.arange(0.0, 0.901, 0.01), 3)

fig, ax = plt.subplots(figsize=(6.5, 4.5))
print(f"{'p_g (bar)':>9s} {'n':>4s} {'f_opt':>6s} {'V_w (L)':>8s} {'apogee (m)':>11s}")
for bar, c in COLORS.items():
    for n, ls in ((1.4, "-"), (1.2, "--")):
        h = np.array([simulate(r, fill=f, p_g=bar * 1e5, n=n).apogee for f in fills])
        i = int(np.argmax(h))
        print(f"{bar:9d} {n:4.1f} {fills[i]:6.2f} {fills[i] * r.V_b * 1e3:8.2f} {h[i]:11.2f}")
        ax.plot(fills, h, color=c, lw=2, ls=ls,
                label=f"{bar} bar" if n == 1.4 else None)
        ax.plot(fills[i], h[i], "o", ms=5, color=c, mec="white", mew=1)
        if n == 1.4:
            ax.text(fills[i] + 0.02, h[i], f"{bar} bar", color=INK, fontsize=8,
                    va="bottom")

ax.plot([], [], color=MUTED, lw=2, ls="-", label="n = 1.4")
ax.plot([], [], color=MUTED, lw=2, ls="--", label="n = 1.2")
ax.set_xlabel("fill fraction f = V_w0 / V_b")
ax.set_ylabel("apogee (m)")
ax.set_xlim(0, 0.9)
ax.set_ylim(bottom=0)
ax.grid(color="#e4e3dd", lw=0.6)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=8, ncol=2)
ax.set_title("Apogee vs fill fraction, 2 L reference rocket, vertical launch",
             fontsize=10, color=INK)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print(f"saved {OUT.relative_to(OUT.parents[2])}")
