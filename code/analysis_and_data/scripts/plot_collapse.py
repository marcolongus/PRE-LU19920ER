import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from itertools import cycle
from typing import List, Tuple

colors = cycle(["blue", "green", "orange"])

# =======================================================================================#
# Data files
# =======================================================================================#
velocities_files = [
    "velocities_uniform",
    "velocities_exponential",
    "velocities_power_law_alpha=4",
    "velocities_uniform_5k",
    "velocities_exponential_5k",
    "velocities_power_law_5k_alpha=4",
]

simulation_files = [
    "uniform",
    "exponential",
    "power_law_alpha=4",
    "uniform_5k",
    "exponential_5k",
    "power_law_5k_alpha=4",
]

# =======================================================================================#
# Constants
# =======================================================================================#
RHO = 1000 / 150**2
TAU_I = 200
SIGMA = 4
PHI = 1.4 * RHO * SIGMA * TAU_I
v_critical = 2 / PHI


# =======================================================================================#
# FUNCTIONS
# =======================================================================================#
def outbreak_size_uniform(v):
    denominator = 2 / PHI - v
    return 1 + v / denominator


def outbreak_size_exponential(v):
    denominator = 2 / PHI - 2 * v
    return 1 + v / denominator


def outbreak_size_power_law(v, gamma=4):
    factor = (gamma - 2) ** 2 / ((gamma - 3) * (gamma - 1))
    denominator = 2 / PHI - factor * v
    return 1 + v / denominator


# =======================================================================================#
# HELPER FUNCTIONS
# =======================================================================================#
def data_loader(
    file_path: str, vel_file: str, sim_file: str
) -> Tuple[np.array, np.array]:
    # Construct full file paths
    vel_file_path = os.path.join(file_path, f"{vel_file}.npy")
    sim_file_path = os.path.join(file_path, f"{sim_file}.npy")
    # Load data from files
    simulation_data = np.load(sim_file_path)
    velocity_data = np.load(vel_file_path)

    return velocity_data, simulation_data


def calculate_interpolation(
    velocity_data: np.array, simulation_data: np.array, num: int
) -> Tuple[np.array, np.array]:
    interp_func = interp1d(velocity_data, simulation_data, kind="cubic")
    v_interpolated = np.linspace(min(velocity_data), max(velocity_data), num=num)
    r_interpolated = interp_func(v_interpolated)
    return v_interpolated, r_interpolated


def pl_square_v(v: np.array, p: float = 4) -> np.array:
    print("Running Power law")
    return ((p - 2) ** 2 / ((p - 3) * (p - 1))) * np.power(v, 2)


def exp_square_v(v: np.array) -> np.array:
    print("Running Exponential")
    return np.power(v, 2) / 2


def uni_square_v(v: np.array) -> np.array:
    print("Running Uniform")
    return np.power(v, 2)


second_moment = cycle([uni_square_v, exp_square_v, pl_square_v])

outbreak_size = cycle(
    [outbreak_size_uniform, outbreak_size_exponential, outbreak_size_power_law]
)

label_sim = cycle(["Uniform Sim.", "Exponential Sim.", "Power Law (q=4) Sim."])
labels = cycle(["Uniform Theo.", "Exponential Theo.", "Power Law (q=4) Theo."])


# =======================================================================================#
# MAIN FUNCTIONS
# =======================================================================================#
def plot_simulations(
    velocities_files: List[str],
    simulation_files: List[str],
    second_moment: cycle,
    N: float = 1,
) -> None:

    iterable = zip(velocities_files, simulation_files, second_moment, colors, label_sim)
    for vel_file, sim_file, v_square, color, label in iterable:
        print(f"Loading: {sim_file}.npy")
        try:
            velocities, r_infi = data_loader("../data/N=5k", vel_file, sim_file)
            linestyle = "-"
        except Exception as e:
            print(e)
            velocities, r_infi = data_loader("../data/N=1k", vel_file, sim_file)
            linestyle = "-"

        v_interpolated, r_interpolated = calculate_interpolation(
            velocities, r_infi, num=50
        )

        velocities = velocities / v_square(velocities)
        # velocities =  1 / velocities

        plt.plot(
            velocities,
            r_infi / N,
            linewidth=3,
            color=color,
            linestyle=linestyle,
            label=label,
        )
        plt.scatter(velocities, r_infi / N, color=color)
        # plt.plot(v_interpolated, r_interpolated / N, linewidth=0.5, color="black")
        # plt.scatter(v_interpolated, r_interpolated / N, color="black", s=1.1)


def plot_theoretical(
    v_thresholds: List[float],
    outbreak: cycle,
    second_moment: cycle,
    epsilon: List[float],
    N: float = 1,
) -> None:

    for v_thresh, outbreak, v_square, eps in zip(
        v_thresholds, outbreak_size, second_moment, epsilon
    ):
        v_theo = np.arange(0.01, v_thresh, eps)
        r_theo = outbreak(v_theo)

        v_theo = v_theo / v_square(v_theo)
        # v_theo =  1 / v_theo

        plt.plot(
            v_theo,
            r_theo / N,
            linewidth=3,
            linestyle="-.",
            color=next(colors),
            label=next(labels),
        )


if __name__ == "__main__":
    # =======================================================================================#
    # SET LABELS AND LIM
    # =======================================================================================#
    x_lim: Tuple[float] = 10, 200
    y_lim: Tuple[float] = 1, 10

    x_label = r"$\langle v \rangle /  \langle v^2 \rangle$"
    y_label = r"$R_{\infty}$"

    # =======================================================================================#
    # SIMULATIONS
    # =======================================================================================#
    plt.xlabel(x_label, fontsize=15)
    plt.ylabel(y_label, fontsize=15)
    plt.xlim(x_lim)
    plt.ylim(y_lim)

    # plot_simulations(velocities_files[3:], simulation_files[3:], second_moment)
    plot_simulations(velocities_files[:3], simulation_files[:3], second_moment)
    # plot_simulations(velocities_files, simulation_files, second_moment)

    plt.legend(fontsize=15)
    plt.tight_layout()
    plt.savefig("../images/simulations_vsaquare_v.png", dpi=300)
    plt.show()
    print("\n\n")

    # =======================================================================================#
    # THEORETICAL
    # =======================================================================================#
    plt.ylabel(y_label, fontsize=15)
    plt.xlabel(x_label, fontsize=15)
    plt.xlim(x_lim)
    plt.ylim(y_lim)

    v_thresholds: List[float] = [2 / PHI, 1 / PHI, (3 / 4) * (2 / PHI)]
    epsilon = [1e-4, 1e-5, 1e-4]

    plot_theoretical(v_thresholds, outbreak_size, second_moment, epsilon)

    plt.legend(fontsize=15)
    plt.tight_layout()
    plt.savefig("../images/theory_vsquare_v.png", dpi=300)
    plt.show()
