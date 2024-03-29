import matplotlib.pyplot as plt
import os
from .config import *


# Plots graph
def plot():
    # Read simulation data from output dump file
    sim_data = np.loadtxt('simulation_data.txt')
    
    ex_data_exists = 0
    if os.path.getsize("uex.txt"):
        ex_data = np.loadtxt('uex.txt')
        ex_data_exists = 1

    # Plot
    x = np.linspace(xmin, xmax, Nx-x_ghost_cells)
    
    time_steps = len(sim_data)
    Dt = Tf / (time_steps-1)

    plt.xlabel('x')
    plt.ylabel('u(x)')

    for t in range(time_steps):
        plt.clf()
        plt.title(f'FVM Simulation after Time Step {t}, t={round(t*Dt, 3)}')

        # Exact Solution
        if ex_data_exists:
            plt.plot(x, ex_data, linestyle=":", marker="o", markersize=1, markerfacecolor='none', label='Exact Solution') 
        
        # Numerical Solution
        plt.plot(x, sim_data[t, :], linestyle=":", marker="o", markersize=1, markerfacecolor='none', label='Numerical Solution') 
        
        plt.legend()
        plt.draw()
        plt.pause(0.08)

    plt.show()


# write data to file
def write_data(filename, u, start, end):
    filename.write(" ".join(map(str, u[start : end+1])) + "\n")


# Print Simulation Parameters
def get_param():
    print("\nNon Identical Kuramoto Equation\n")
    print("X Domain Limits (xmin, xmax):", xmin, ", ", xmax)
    print("X Domain Length (Lx):", Lx)
    print("Number of Spatial Points (Nx):", Nx - x_ghost_cells)
    print("Cell Width (dx):", dx, "\n")
    print("Y Domain Limits (ymin, ymax):", ymin, ", ", ymax)
    print("Y Domain Length (Ly):", Ly)
    print("Number of Y Points (Ny):", Ny - y_ghost_cells)
    print("Y step (dy):", dx, "\n")
    print("Stability Parameter (CFL Number):", cfl, "\n")
    print("Omega, Coupling Strength:", om, ", ", K, "\n")
    print("Final Time (Tf):", Tf, "\n")
    


