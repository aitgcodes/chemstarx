import matplotlib.pyplot as plt
import sys

def plot_pes_data(file_path, plot_type='x'):
    """
    Plots energy vs x or y from a .dat file.

    Parameters:
    - file_path: str, path to the .dat file.
    - plot_type: str, 'x' or 'y' to specify which variable to plot against energy.
    """
    x = []
    y = []
    energy = []
    
    conversion_factor = 627.509474  # Factor to convert energy

    with open(file_path, 'r') as f:	   
        
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            data = line.split()
            x.append(float(data[0]))
            y.append(float(data[1]))
            #energy_initial=data[2].lstrip('(').rstrip(',')
            energy_value = float(data[2].lstrip('(').rstrip(',')) 
            #energy_diff=float(energy_value)-float(energy_initial)
            energy.append(energy_value*conversion_factor)

    if plot_type == 'x':
        plt.plot(x, energy, 'o-')
        plt.xlabel('CI Bond Distance')
        plt.ylabel('Energy(in kcal/mol)')
        plt.title('Energy vs CI Bond Distance')
    elif plot_type == 'y':
        plt.plot(y, energy, 'o-')
        plt.xlabel('CCl Bond Distance')
        plt.ylabel('Energy')
        plt.title('Energy vs CCl Bond Distance')
    else:
        raise ValueError("Invalid plot_type. Choose 'x' or 'y'.")

    ax = plt.gca()
    ax.ticklabel_format(useOffset=False)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 plot_pes_data.py <file_path> <plot_type>")
        sys.exit(1)

    file_path = sys.argv[1]
    plot_type = sys.argv[2]
    plot_pes_data(file_path, plot_type)

