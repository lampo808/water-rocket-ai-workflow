# code

Python simulation of the water rocket. Equation labels refer to
`docs/physics.md`. Run from the repository root:

```sh
uv run python code/fig_trajectory.py      # docs/figures/fig_trajectory.png
uv run python code/fig_apogee_vs_fill.py  # docs/figures/fig_apogee_vs_fill.png
```

- `rocket.py`: the model (parameters, three phases, `simulate`).
- `fig_trajectory.py`: one flight vs time; prints the event values.
- `fig_apogee_vs_fill.py`: apogee vs fill fraction; prints the optima.
