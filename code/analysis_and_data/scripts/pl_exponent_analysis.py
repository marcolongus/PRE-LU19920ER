import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from typing import Dict, Tuple

# =====================================================================================#
# CONSTANTS
# =====================================================================================#
RHO: float = 1000 / 150**2
TAU_I: float = 200
SIGMA: float = 4
PHI: float = 1.4 * RHO * SIGMA * TAU_I
N: float = 1000

v_uniform_crit: float = 2 / PHI

# =====================================================================================#
# DATA FILES
# =====================================================================================#
file_alpha_mapping = {
    "velocities_power_law_alpha=3.1": 3.1,
    "velocities_power_law_alpha=3.5": 3.5,
    "velocities_power_law_alpha=4": 4,
    "velocities_power_law_alpha=5": 5,
    "velocities_power_law_alpha=6": 6,
    "velocities_power_law_alpha=8": 8,
    "velocities_power_law_alpha=10": 10,
}


# =====================================================================================#
# HELPER FUNCTIONS
# =====================================================================================#
def calculate_interpolation(
    velocity_data: np.array, simulation_data: np.array, num: int
) -> Tuple[np.array, np.array]:
    interp_func = interp1d(velocity_data, simulation_data, kind="cubic")
    v_interpolated = np.linspace(min(velocity_data), max(velocity_data), num=num)
    r_interpolated = interp_func(v_interpolated)
    return v_interpolated, r_interpolated


def threshold_detection(simulation: np.array, threshold: float = 0.012) -> int | None:
    indices_above_threshold = np.where(simulation >= threshold)[0]
    return indices_above_threshold.min() if len(indices_above_threshold) > 0 else None


def alpha_curve(q: np.array) -> np.array:
    """Plot v_pl_crit / v_uni against pl p exponent"""
    return (q - 3) * (q - 1) / (q - 2) ** 2


def calculate_critical_velocities(files: Dict[str, float], folder="N=1k") -> np.array:
    v_critical_values = []
    for vel_file, alpha in file_alpha_mapping.items():
        sim_file = vel_file.replace("velocities_", "")
        # Load data
        velocities = np.load(f"../data/{folder}/{vel_file}.npy")
        r_infi = np.load(f"../data/{folder}/{sim_file}.npy") / N

        velocities, r_infi = calculate_interpolation(velocities, r_infi, num=500)

        if alpha < 6 or alpha > 8:
            plt.plot(velocities, r_infi * N, label=f"q={alpha}", linewidth=4)
        # plt.scatter(velocities, r_infi * N)

        # plt.plot(v_inter, r_inter * N, color="black")
        # plt.scatter(v_inter, r_inter * N, color="black")

        threshold_index = threshold_detection(r_infi)

        if threshold_index is not None:
            v_critical_values.append(velocities[threshold_index])

    return np.array(v_critical_values)


def calculate_uniform_threshold(folder="N=1k") -> Tuple[np.array]:
    file_path = f"../data/{folder}/velocities_uniform.npy"
    velocities = np.load(file_path)
    v_c = velocities[
        threshold_detection(np.load(file_path.replace("velocities_", "")) / N)
    ]
    return velocities, v_c


# =====================================================================================#
# PLOTS SIMULATIONS
# =====================================================================================#
plt.xlim(0.025, 0.06)
plt.ylim(10, 100)
plt.ylabel(r"$R_{\infty}$")
plt.xlabel(r"$\langle v_c^{PL} \rangle$")
v_critical_values = calculate_critical_velocities(file_alpha_mapping, folder="N=1k")

plt.legend()
plt.tight_layout()
plt.savefig("../images/q-curves-end.png", dpi=300)
plt.show()

# =====================================================================================#
# PLOTS SIMULATIONS q-curve
# =====================================================================================#
velocities, v_c = calculate_uniform_threshold(folder="N=1k")
plt.plot(
    list(file_alpha_mapping.values()),
    np.array(v_critical_values) / v_c,
    color="black",
    label="Simulations",
    linewidth=4,
)
plt.scatter(
    list(file_alpha_mapping.values()), v_critical_values / v_c, color="black", s=70
)


# =====================================================================================#
# PLOTS THEORETICAL  q-curve
# =====================================================================================#
tick_fontsize = 20
label_fontsize = 30

p_values = np.arange(3.5, 10, 0.01)
plt.xlabel("q", fontsize=label_fontsize)
plt.ylabel(r"$ \langle \tilde v \rangle_c^P$", fontsize=label_fontsize, ha="right")
plt.plot(
    p_values, alpha_curve(p_values), label="Theory", linewidth=4, linestyle="dashed"
)

xticks = [3, 5, 7, 9]
yticks = [0.6, 0.8, 1]
plt.xticks(xticks, fontsize=tick_fontsize)
plt.yticks(yticks, fontsize=tick_fontsize)

plt.minorticks_on()
plt.legend(fontsize=20)

plt.tight_layout()
plt.savefig("../images/p_comparison.png")
plt.show()
