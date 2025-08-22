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
labels = cycle(["Uniform", "Exponential", "Power Law (q=4)"])


# =======================================================================================#
# MAIN FUNCTIONS
# =======================================================================================#
def plot_simulations(
    velocities_files: List[str],
    simulation_files: List[str],
    second_moment: cycle,
    N: float = 1,
) -> None:
    for vel_file, sim_file, color in zip(velocities_files, simulation_files, colors):
        print(f"Loading: {sim_file}.npy")
        try:
            velocities, r_infi = data_loader("data/N=1k", vel_file, sim_file)
            linestyle = "-"
        except:
            velocities, r_infi = data_loader("data/N=1k", vel_file, sim_file)
            linestyle = "-"

        v_interpolated, r_interpolated = calculate_interpolation(
            velocities, r_infi, num=50
        )
        # v_square =  next(second_moment)(velocities)
        # velocities =  velocities / v_square
        # velocities =  1 / velocities

        plt.plot(
            velocities,
            r_infi / N,
            linewidth=4,
            color=color,
            linestyle=linestyle,
            label=next(labels),
        )
        plt.scatter(velocities, r_infi / N, color=color, s=100)
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

        plt.plot(
            v_theo,
            r_theo / N,
            linewidth=5,
            linestyle="dashed",
            color=next(colors),
            label=next(labels),
        )


if __name__ == "__main__":

    # plt.rcParams['ytick.right']  = True
    # plt.rcParams['ytick.left']   = True

    # plt.rcParams['ytick.labelright'] = True
    # plt.rcParams['ytick.labelleft'] = False

    x_lim: Tuple[float] = 0.01, 0.04
    y_lim: Tuple[float] = 1, 10

    x_label = r"$\langle v \rangle$"
    y_label = r"$\langle n_r \rangle$"

    ticks_fontsize = 20
    lab_fontsize = 30

    plt.minorticks_on()

    # =======================================================================================#
    # SIMULATIONS
    # =======================================================================================#
    plt.xlabel(x_label, fontsize=lab_fontsize)
    plt.ylabel(y_label, fontsize=lab_fontsize)
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.xticks([0.015, 0.025, 0.035], fontsize=ticks_fontsize)
    plt.yticks([1, 4, 7, 10], fontsize=ticks_fontsize)

    # plot_simulations(velocities_files[3:], simulation_files[3:], second_moment)
    plot_simulations(velocities_files[:3], simulation_files[:3], second_moment)

    plt.legend(fontsize=12, loc=4)
    plt.tight_layout()
    plt.savefig("images/n_R_simulation.png", dpi=300)
    plt.show()

    # =======================================================================================#
    # THEORETICAL
    # =======================================================================================#
    plt.ylabel(y_label, fontsize=lab_fontsize)
    plt.xlabel(x_label, fontsize=lab_fontsize)
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.xticks([0.015, 0.025, 0.035], fontsize=ticks_fontsize)
    plt.yticks([1, 4, 7, 10], fontsize=ticks_fontsize)

    plt.minorticks_on()

    v_thresholds = [2 / PHI, 1 / PHI, (3 / 4) * (2 / PHI)]
    epsilon = [1e-4, 1e-5, 1e-4]

    plot_theoretical(v_thresholds, outbreak_size, second_moment, epsilon)

    plt.legend(fontsize=12, loc=4)
    plt.tight_layout()
    plt.savefig("images/n_R_theory.png", dpi=300)
    plt.show()
