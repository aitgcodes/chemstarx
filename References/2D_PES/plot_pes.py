import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys

def plot_pes_data(file_path, mode='2d', plot_type='x'):
    """
    Plots energy vs x or y for 2D or 3D PES surface plot from a .dat file.

    Parameters:
    - file_path: str, path to the .dat file.
    - mode: str, '2d' or '3d' to specify the type of plot.
    - plot_type: str, 'x' or 'y' to specify which variable to plot against energy in 2D mode.
    """
    x = []
    y = []
    energy = []

    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            data = line.split()
            x.append(float(data[0]))
            y.append(float(data[1]))
            energy_value = data[2].strip('(),')
            energy.append(float(energy_value) * 627.509)  # Convert Ha to kcal/mol

    if mode == '2d':
        if plot_type == 'x':
            plt.plot(x, energy, 'o-')
            plt.xlabel('X')
            plt.ylabel('Energy (kcal/mol)')
            plt.title('Energy vs X')
        elif plot_type == 'y':
            plt.plot(y, energy, 'o-')
            plt.xlabel('Y')
            plt.ylabel('Energy (kcal/mol)')
            plt.title('Energy vs Y')
        else:
            raise ValueError("Invalid plot_type. Choose 'x' or 'y'.")
        plt.grid(True)
        plt.show()

    elif mode == '3d':
        x = np.array(x)
        y = np.array(y)
        energy = np.array(energy)

        # Create grid for 3D plot
        X, Y = np.meshgrid(np.unique(x), np.unique(y))
        Z = energy.reshape(len(np.unique(x)), len(np.unique(y)))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap='viridis')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Energy (kcal/mol)')
        ax.set_title('3D Potential Energy Surface')
        fig.colorbar(surf, shrink=0.5, aspect=5)

        # Adjust view angle for better visualization
        ax.view_init(elev=30, azim=120)

        plt.show()

    else:
        raise ValueError("Invalid mode. Choose '2d' or '3d'.")

if __name__ == '__main__':
    if len(sys.argv) not in [3, 4]:
        print("Usage: python3 plot_pes_data.py <file_path> <mode> [<plot_type>]")
        sys.exit(1)

    file_path = sys.argv[1]
    mode = sys.argv[2]
    plot_type = sys.argv[3] if len(sys.argv) == 4 else 'x'
    plot_pes_data(file_path, mode, plot_type)


