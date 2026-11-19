"""Figure docs/figures/fig_trajectory.png: one flight vs time.

Case: reference rocket (code/rocket.py defaults), fill 0.25 (0.5 L in
2 L), gauge pressure 2 bar, n = 1.4. Panels: height, velocity, thrust,
bottle pressure. Phase boundaries marked. Prints the event values.
"""

from pathlib import Path

import matplotlib.pyplot as plt

from rocket import Rocket, simulate

OUT = Path(__file__).resolve().parent.parent / "docs" / "figures" / "fig_trajectory.png"
INK, MUTED, LINE = "#1f1f1e", "#6b6a64", "#2a78d6"

r = Rocket()
fl = simulate(r, fill=0.25, p_g=2.0e5)
ev = fl.events

fig, ax = plt.subplots(4, 1, figsize=(6.5, 8.5), sharex=False)
t_burn = ev["t_burn"]

# Height and velocity over the full flight to apogee.
ax[0].plot(fl.t, fl.z, color=LINE, lw=2)
ax[0].set_ylabel("height z (m)")
ax[1].plot(fl.t, fl.v, color=LINE, lw=2)
ax[1].set_ylabel("velocity v (m/s)")

# Thrust and pressure only during the powered phases (zoom).
pw = fl.phase < 3
ax[2].plot(fl.t[pw] * 1e3, fl.thrust[pw], color=LINE, lw=2)
ax[2].set_ylabel("thrust (N)")
ax[3].plot(fl.t[pw] * 1e3, fl.p[pw] / 1e5, color=LINE, lw=2)
ax[3].axhline(r.p_a / 1e5, color=MUTED, lw=1, ls=":")
ax[3].text(1, r.p_a / 1e5, " ambient", color=MUTED, va="bottom", fontsize=8)
ax[3].set_ylabel("bottle pressure (bar, abs.)")
ax[2].set_xlabel("time (ms)")
ax[3].set_xlabel("time (ms)")
ax[1].set_xlabel("time (s)")
ax[0].set_xlabel("time (s)")

# Phase boundaries: end of water, end of air.
for a, scale in ((ax[0], 1), (ax[1], 1), (ax[2], 1e3), (ax[3], 1e3)):
    for key in ("t_water", "t_burn"):
        a.axvline(ev[key] * scale, color=MUTED, lw=1, ls="--")
    a.grid(color="#e4e3dd", lw=0.6)
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
    a.tick_params(colors=INK, labelsize=8)
ax[2].text(ev["t_water"] * 1e3, ax[2].get_ylim()[1] * 0.9, " water out",
           color=MUTED, fontsize=8)
ax[2].text(ev["t_burn"] * 1e3, ax[2].get_ylim()[1] * 0.75, "air out ",
           color=MUTED, fontsize=8, ha="right")
ax[0].annotate(f"apogee {ev['apogee_z']:.1f} m", (ev["apogee_t"], ev["apogee_z"]),
               xytext=(-90, -15), textcoords="offset points", fontsize=8, color=INK)

fig.suptitle("Vertical flight: 2 L bottle, fill 0.25, 2 bar gauge, n = 1.4",
             fontsize=10, color=INK)
fig.tight_layout()
fig.savefig(OUT, dpi=150)

for k, v in ev.items():
    print(f"{k:16s} {float(v):.4g}")
print(f"{'coast_numeric':16s} {ev['apogee_z'] - ev['z_burn']:.4g}")
print(f"{'peak thrust N':16s} {fl.thrust.max():.4g}")
print(f"saved {OUT.relative_to(OUT.parents[2])}")
