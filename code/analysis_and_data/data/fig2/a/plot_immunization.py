import numpy as np
import matplotlib.pyplot as plt
from typing import List
from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["ytick.right"] = True
plt.rcParams["ytick.left"] = True

plt.rcParams["ytick.labelright"] = True
plt.rcParams["ytick.labelleft"] = False

folders = ["Exponential", "Power Law", "Uniform"]
markers = cycle(["H", "s"])

# ============================================================================================
# EXPONENTIAL AND POWER LAW
# ============================================================================================
files: List[int] = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70]
color = ["green", "orange"]
plt.ylim(0.01, 0.88)
plt.xlim(-1, 71)

x_attack = 10 * np.array(files)
for col, folder in zip(color, folders[0:2]):
    print(folder)
    y_random = []
    y_directed = []

    # Random
    for a, file in zip(x_attack, files):
        data_random = np.loadtxt(f"{folder}/data/Random/{file} %/{file}.txt")
        size_random = ((data_random[:, 0] - a) / (1000)).mean()
        y_random.append(size_random)
        print(round(size_random, 2), file, "random")

    # Directed
    for a, file in zip(x_attack, files):
        data_directed = np.loadtxt(f"{folder}/data/Directed/{file} %/{file}.txt")
        size_directed = ((data_directed[:, 0] - a) / (1000)).mean()
        y_directed.append(size_directed)
        print(round(size_directed, 2), file, "directed")

    x = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70]

    marker = next(markers)
    plt.plot(
        x,
        y_random,
        linestyle="dashed",
        label=folder + " (RVS)",
        color=col,
        linewidth=4,
    )
    plt.scatter(x, y_random, color=col, marker=marker, s=150)

    np.save(f"y_fig2_{folder}_random.npy", y_random)

    x = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70]
    plt.plot(x, y_directed, color=col, label=folder + " (DVS)", linewidth=4)
    plt.scatter(x, y_directed, color=col, marker=marker, s=150)
    print()

    np.save("x_fig2.npy", x)
    np.save(f"y_fig2_{folder}_directed.npy", y_directed)

print(100 * "=")
print()


# ============================================================================================
# UNIFORMS
# ============================================================================================
files = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70]
x = 10 * np.array(files)

for folder in [folders[2]]:
    y = []
    for a, file in zip(x, files):
        data = np.loadtxt(f"{folder}/data/Random/{file} %/{file}.txt")

        # if uses the imnmune state or refractory
        if file in [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70]:
            size = ((data[:, 0] - a) / (1000)).mean()
        else:
            size = ((data[:, 0]) / (1000)).mean()

        y.append(size)
        print(round(size, 1), file)

    plt.plot(
        files, y, label=folder + " (RVS)", linewidth=4, linestyle="dashed", color="blue"
    )

    np.save(f"y_fig2_{folder}.npy", y)
    plt.scatter(files, y, s=150, color="blue")

# ============================================================================================
# COSMETIC
# ============================================================================================
plt.xlim(-1, 71)
plt.xlabel(r"$f$ (%)", fontsize=25)
plt.ylabel(r"$\frac{\langle n_R \rangle}{N}$ ", fontsize=25, rotation=0, ha="right")
handles, labels = plt.gca().get_legend_handles_labels()
order = [
    4,
    0,
    2,
    1,
    3,
]  # Specify the order in which you want the legend entries to appear

plt.legend(
    [handles[idx] for idx in order], [labels[idx] for idx in order], fontsize=6, loc=3
)

plt.xticks([0, 20, 40, 60], fontsize=20)  # Change 12 to whatever size you prefer
plt.yticks([0.2, 0.4, 0.6, 0.8, 1], fontsize=20)

# plt.semilogy()
# plt.semilogy()
# plt.loglog()

plt.tight_layout()
plt.savefig("inmunization_semilogy.png")
plt.show()
