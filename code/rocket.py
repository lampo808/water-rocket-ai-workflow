"""Water rocket model: vertical 1D flight in three phases.

Phases (equation labels refer to docs/physics.md):
  1. water thrust:  quasi-steady Bernoulli, polytropic air expansion
  2. air thrust:    quasi-steady flow of air through a convergent nozzle,
                    choked or subsonic
  3. ballistic:     gravity and quadratic drag, up to the apogee

SI units throughout. Pressures are absolute unless the name ends in _g
(gauge = absolute - ambient).
"""

from dataclasses import dataclass, field

import numpy as np
from scipy.integrate import solve_ivp

# --- Physical constants (textbook values) ---------------------------------
G = 9.80665          # standard gravity, m/s^2
R_AIR = 287.05       # specific gas constant of dry air, J/(kg K)
GAMMA = 1.4          # heat capacity ratio of dry air, -
RHO_W = 997.8        # density of water at 22 degC, kg/m^3


@dataclass
class Rocket:
    """Rocket and ambient parameters.

    Defaults: the rocket of Barrio-Perotti et al. 2010 (sources/
    barrioperotti2010theoretical.md, section 5) and the drag coefficient
    measured on it by Barrio-Perotti et al. 2009 (sources/
    barrioperotti2009experimental.md).
    """
    V_b: float = 2.0e-3       # bottle volume, m^3 (2 L)
    m_b: float = 0.1332       # empty rocket mass, kg
    D: float = 0.106          # bottle diameter, m
    d: float = 0.0215         # nozzle diameter, m
    C_D: float = 0.345        # drag coefficient, frontal area pi D^2/4
    p_a: float = 1.020e5      # ambient pressure, Pa (1020 mbar)
    T_a: float = 295.15       # ambient temperature, K (22 degC)

    @property
    def A_b(self):            # bottle cross-section, m^2
        return np.pi * self.D**2 / 4

    @property
    def A_n(self):            # nozzle cross-section, m^2
        return np.pi * self.d**2 / 4

    @property
    def rho_a(self):          # ambient air density, kg/m^3 (ideal gas)
        return self.p_a / (R_AIR * self.T_a)

    def drag(self, v):
        """Quadratic drag force, N, opposite to v (eq. D1)."""
        return 0.5 * self.rho_a * self.C_D * self.A_b * v * abs(v)


@dataclass
class Flight:
    """Result of one simulation. Arrays are concatenated over phases."""
    t: np.ndarray             # time, s
    z: np.ndarray             # height, m
    v: np.ndarray             # velocity, m/s
    thrust: np.ndarray        # thrust, N
    p: np.ndarray             # absolute pressure in the bottle, Pa
    phase: np.ndarray         # 1 water, 2 air, 3 ballistic
    events: dict = field(default_factory=dict)  # named scalar results

    @property
    def apogee(self):
        return self.events["apogee_z"]


def _on_pad(z, v, a):
    """Rocket resting on the pad: no motion while net force points down."""
    return z <= 0.0 and v <= 0.0 and a < 0.0


# --- Phase 1: water thrust -------------------------------------------------

def water_phase(r, p0, V0, n, m_air, head=False, t_span=(0.0, 5.0)):
    """Integrate the water phase.

    State y = [z, v, V], V = air volume in the bottle, m^3.
    Ends when the water is exhausted (V = V_b) or the driving pressure
    has dropped to zero with water left.

    head=False: driving pressure p - p_a (eq. W2).
    head=True:  sensitivity case, driving pressure
                p - p_a + rho_w (g + a) h (eq. W2h), with the water
                column height h = (V_b - V)/A_b (cylindrical bottle).
    """
    k_area = 1.0 - (r.A_n / r.A_b) ** 2      # area-ratio factor of eq. (W2)

    def pressure(V):
        return p0 * (V0 / V) ** n                         # eq. (W1)

    def balance(y):
        """Return (driving pressure Pa, acceleration m/s^2, thrust N).

        Thrust F = rho_w A_n u_e^2 = 2 A_n dp / k_area (eqs. W2, W5).
        With the head, dp depends on a; the balance (W6) is linear in a
        and is solved for a explicitly (eq. W6h).
        """
        z, v, V = y
        m = r.m_b + m_air + RHO_W * (r.V_b - V)            # eq. (W4)
        h = (r.V_b - V) / r.A_b if head else 0.0           # column, m
        c = 2.0 * r.A_n / k_area                           # F = c * dp
        dp0 = pressure(V) - r.p_a + RHO_W * G * h          # dp at a = 0
        # (W6): m a = c (dp0 + rho_w a h) - F_D - m g
        a = (c * dp0 - r.drag(v) - m * G) / (m - c * RHO_W * h)
        if _on_pad(z, v, a):
            a = 0.0
        dp = dp0 + RHO_W * a * h
        if dp <= 0.0:                    # no outflow: jet stopped
            dp = 0.0
            a = (-r.drag(v) - m * G) / m
            if _on_pad(z, v, a):
                a = 0.0
        return dp, a, c * dp

    def rhs(t, y):
        dp, a, _ = balance(y)
        u = np.sqrt(2.0 * dp / (RHO_W * k_area))           # eq. (W2)
        return [y[1], a, r.A_n * u]                        # eq. (W3)

    def empty(t, y):                     # water exhausted
        return y[2] - r.V_b * (1.0 - 1e-9)
    empty.terminal, empty.direction = True, 1

    def stalled(t, y):                   # driving pressure reaches zero
        return balance(y)[0] - 1e-6 * r.p_a
    stalled.terminal, stalled.direction = True, -1

    sol = solve_ivp(rhs, t_span, [0.0, 0.0, V0], events=[empty, stalled],
                    rtol=1e-9, atol=[1e-9, 1e-9, 1e-12], max_step=1e-3)
    if sol.status != 1:                  # guard: an end event must fire
        raise RuntimeError("water phase: no end event reached")
    V = sol.y[2]
    p = pressure(V)
    thrust = np.array([balance(yi)[2] for yi in sol.y.T])
    water_left = RHO_W * (r.V_b - V[-1])
    starved = sol.t_events[1].size > 0
    if not starved:
        water_left = 0.0                 # event at V_b (1e-9 tolerance)
    return sol, p, thrust, water_left, starved


# --- Phase 2: air thrust ---------------------------------------------------

CRIT = (2.0 / (GAMMA + 1.0)) ** (GAMMA / (GAMMA - 1.0))   # eq. (A3), 0.528
CP = GAMMA * R_AIR / (GAMMA - 1.0)                         # J/(kg K)


def nozzle(r, p, T):
    """Mass flow, exit velocity and exit pressure of air through the
    convergent nozzle, from bottle stagnation state (p, T).
    Returns (mdot kg/s, u_e m/s, p_e Pa)."""
    if p <= r.p_a:
        return 0.0, 0.0, r.p_a
    if r.p_a / p <= CRIT:                                   # choked
        p_e = p * CRIT                                      # eq. (A4)
        T_e = T * 2.0 / (GAMMA + 1.0)
        u_e = np.sqrt(GAMMA * R_AIR * T_e)
    else:                                                   # subsonic
        p_e = r.p_a                                         # eq. (A5)
        T_e = T * (r.p_a / p) ** ((GAMMA - 1.0) / GAMMA)
        u_e = np.sqrt(2.0 * CP * (T - T_e))
    rho_e = p_e / (R_AIR * T_e)
    return rho_e * u_e * r.A_n, u_e, p_e                   # eq. (A6)


def air_phase(r, z0, v0, t0, p1, m1, n, extra_mass=0.0):
    """Integrate the air phase.

    State y = [z, v, m_air]. Bottle gas follows p = p1 (rho/rho1)^n
    (eq. A1). Ends when p = p_a.
    """
    rho1 = m1 / r.V_b

    def state(m):
        rho = m / r.V_b
        p = p1 * (rho / rho1) ** n                          # eq. (A1)
        T = p / (rho * R_AIR)                               # eq. (A2)
        return p, T

    def thrust_of(m):
        p, T = state(m)
        mdot, u_e, p_e = nozzle(r, p, T)
        return mdot * u_e + (p_e - r.p_a) * r.A_n, mdot     # eq. (A7)

    def rhs(t, y):
        z, v, m = y
        F, mdot = thrust_of(m)
        M = r.m_b + extra_mass + m
        a = (F - r.drag(v)) / M - G                         # eq. (A8)
        if _on_pad(z, v, a):
            a = 0.0
        return [v, a, -mdot]

    # Air mass at which p = p_a.
    m_pa = m1 * (r.p_a / p1) ** (1.0 / n)

    def end(t, y):
        return y[2] - m_pa * (1.0 + 1e-9)
    end.terminal, end.direction = True, -1

    sol = solve_ivp(rhs, (t0, t0 + 5.0), [z0, v0, m1], events=end,
                    rtol=1e-9, atol=[1e-9, 1e-9, 1e-12], max_step=1e-4)
    p = np.array([state(m)[0] for m in sol.y[2]])
    thrust = np.array([thrust_of(m)[0] for m in sol.y[2]])
    return sol, p, thrust


# --- Phase 3: ballistic ----------------------------------------------------

def ballistic_phase(r, z0, v0, t0, mass):
    """Integrate from burnout to apogee (v = 0). State y = [z, v]."""
    def rhs(t, y):
        z, v = y
        a = -r.drag(v) / mass - G                           # eq. (B1)
        if _on_pad(z, v, a):
            a = 0.0
        return [v, a]

    def top(t, y):
        return y[1]
    top.terminal, top.direction = True, -1

    if v0 <= 0.0:                    # no lift-off: stays on the pad
        return None
    return solve_ivp(rhs, (t0, t0 + 60.0), [z0, v0], events=top,
                     rtol=1e-10, atol=1e-10, max_step=1e-2)


def coast_height(r, v_max, mass):
    """Analytic coast height with quadratic drag (eq. B2, Fischer 2020
    eq. 35)."""
    psi = r.rho_a * r.C_D * r.A_b / (2.0 * mass)
    return np.log(1.0 + psi * v_max**2 / G) / (2.0 * psi)


# --- Full flight -----------------------------------------------------------

def simulate(r=None, fill=0.25, p_g=2.0e5, n=GAMMA, head=False):
    """Simulate one vertical flight.

    fill: initial water volume / bottle volume, 0 <= fill < 1
    p_g:  initial gauge pressure, Pa
    n:    polytropic exponent of the bottle gas (1.4 = dry adiabat)
    head: include the inertial head of the water column (eq. W2h)
    """
    r = r or Rocket()
    p0 = r.p_a + p_g                                  # absolute, Pa
    V0 = (1.0 - fill) * r.V_b                         # initial air volume
    m_air = p0 * V0 / (R_AIR * r.T_a)                 # gas at ambient T
    ev = {"fill": fill, "p_g": p_g, "n": n, "head": head, "m_air0": m_air}
    if p0 <= r.p_a:                       # guard: no overpressure, no flight
        ev.update(apogee_z=0.0, apogee_t=0.0)
        zero = np.zeros(1)
        return Flight(zero, zero, zero, zero, np.full(1, p0), np.ones(1), ev)
    T_parts, Z, Vv, F, P, PH = [], [], [], [], [], []

    # Phase 1: water. Skipped when there is no water.
    z, v, t, water_left, starved = 0.0, 0.0, 0.0, 0.0, False
    p1 = p0
    if fill > 0.0:
        s1, p, thr, water_left, starved = water_phase(r, p0, V0, n, m_air, head)
        T_parts.append(s1.t); Z.append(s1.y[0]); Vv.append(s1.y[1])
        F.append(thr); P.append(p); PH.append(np.full(s1.t.size, 1))
        t, z, v = s1.t[-1], s1.y[0, -1], s1.y[1, -1]
        p1 = p[-1]
        ev.update(t_water=t, v_water=v, z_water=z, p_water=p1,
                  water_left=water_left, starved=starved)

    # Phase 2: air. Absent when the pressure is already ambient.
    m_burn = r.m_b + water_left
    if p1 > r.p_a * (1.0 + 1e-6):
        T1 = r.T_a * (p1 / p0) ** ((n - 1.0) / n)     # polytropic, eq. (A0)
        m1 = p1 * r.V_b / (R_AIR * T1)
        s2, p, thr = air_phase(r, z, v, t, p1, m1, n, extra_mass=water_left)
        T_parts.append(s2.t); Z.append(s2.y[0]); Vv.append(s2.y[1])
        F.append(thr); P.append(p); PH.append(np.full(s2.t.size, 2))
        t, z, v = s2.t[-1], s2.y[0, -1], s2.y[1, -1]
        m_burn += s2.y[2, -1]
        ev.update(t_air=t - ev.get("t_water", 0.0), v_air=v, z_air=z)
    else:
        m_burn += m_air

    ev.update(t_burn=t, v_burn=v, z_burn=z, m_burn=m_burn)

    # Phase 3: ballistic.
    s3 = ballistic_phase(r, z, v, t, m_burn)
    if s3 is None:
        ev.update(apogee_z=z, apogee_t=t)
    else:
        T_parts.append(s3.t); Z.append(s3.y[0]); Vv.append(s3.y[1])
        F.append(np.zeros(s3.t.size)); P.append(np.full(s3.t.size, r.p_a))
        PH.append(np.full(s3.t.size, 3))
        ev.update(apogee_z=s3.y[0, -1], apogee_t=s3.t[-1],
                  coast_analytic=coast_height(r, v, m_burn))

    return Flight(np.concatenate(T_parts), np.concatenate(Z),
                  np.concatenate(Vv), np.concatenate(F), np.concatenate(P),
                  np.concatenate(PH), ev)
