import matplotlib.pyplot as plt
import os
from .config import *

# Plots graph
def plot():
    # Read simulation data from output dump file
    sim_data = np.loadtxt('simulation_data.txt')
    
    ex_data_exists = os.path.getsize("uex.txt") > 0
    if ex_data_exists:
        ex_data = np.loadtxt('uex.txt')

    # Plot
    x = np.linspace(xmin, xmax, Nx-ghost_cells)
    
    time_steps = len(sim_data)
    Dt = Tf / (time_steps-1)

    plt.xlabel(r'$\theta$')
    plt.ylabel(r'$\mu(\theta)$')

    for t in range(time_steps):
        plt.clf()
        plt.title(f'FVM Simulation after Time Step {t}, t={round(t*Dt, 3)}')
        # plt.title('FVM Sim, LF num-flux; IDKuramoto Equation, Polynomial Initial Data')

        # Exact Solution
        if ex_data_exists:
            plt.plot(x, ex_data, linestyle=":", marker="o", markersize=1, markerfacecolor='none', label='Exact Solution') 
        # Numerical Solution
        plt.plot(x, sim_data[t, :], linestyle=":", marker="o", markersize=1, markerfacecolor='none', label='Numerical Solution') 
        
        # plt.savefig(idkuramoto/steps/f'{t}.png', bbox_inches='tight')
        plt.legend()
        plt.draw()
        plt.pause(0.08)

    plt.show()


# write data to file
def write_data(filename, u, start, end):
    filename.write(" ".join(map(str, u[start : end+1])) + "\n")


# Print Simulation Parameters
def get_param():
    print("\nIdentical Kuramoto Equation\n")
    print("Domain Limits (xmin, xmax):", xmin, ", ", xmax)
    print("Domain Length (L):", L)
    print("Number of Spatial Points (Nx):", Nx - ghost_cells)
    print("Cell Width (dx):", dx, "\n")
    print("Stability Parameter (CFL Number):", cfl, "\n")
    print("Omega, Coupling Strength:", om, " ", K, "\n")
    print("Final Time (Tf):", Tf, "\n")
    


