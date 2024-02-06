import numpy as np

'''
    Config file to set Simulation Parameters
'''

xmin, xmax = 0, 2*np.pi  # Domain limits
L = abs(xmax - xmin)  # Domain Length
ghost_cells = 1  # Number of ghost cells
Nx = 512 + ghost_cells  # Number of spatial points
dx = L / (Nx-1)  # Cell width
# dx = 0.01 # Cell width
# Nx = int(L/dx) + 1 + ghost_cells # Number of spatial points
x = np.linspace(xmin + dx/2, xmax - dx/2, Nx)   # Spatial grid

cfl = 0.35  # Stability Parameter - CFL Number

Tf = 1.0  # Final time / Total Time

first_cell, last_cell = 1, Nx-1  # j domain Limits


om = None # Natural Frequency
K = 1 # Coupling Strength


# Returns 
def flux(V_U, u, x_index):
    pass

