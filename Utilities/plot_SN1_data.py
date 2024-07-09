import matplotlib.pyplot as plt
import numpy as np
import sys

def plot_bond_length_vs_energy(file_path):
    """
    Plots bond length vs. energy from a .dat file.

    Parameters:
    - file_path: str, path to the .dat file.
    """
    bond_length = []
    energy = []

    conversion_factor = 627.509  # Convert Ha to kcal/mol

    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            data = line.split()
            bond_length.append(float(data[0]))
            energy_value = data[1].strip('(),')
            energy.append(float(energy_value) * conversion_factor)

    bond_length = np.array(bond_length)
    energy = np.array(energy)

    plt.plot(bond_length, energy, 'o-')
    plt.xlabel('Bond Length (Å)')
    plt.ylabel('Energy (kcal/mol)')
    plt.title('Bond Length vs Energy')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 plot_bond_length_vs_energy.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    plot_bond_length_vs_energy(file_path)

