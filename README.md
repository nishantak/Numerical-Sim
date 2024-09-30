# Numerical Simulation: PINN Approach
- Explicit Finite Volume Numerical Analysis Scheme <br> 

<img></img> <img src="sim_gifs/td.gif" alt="trspt_disc" width="23%"></img> <img src="sim_gifs/bs.gif" alt="burg_sin" width="23.5%"></img> <img src="sim_gifs/idp.gif" alt="id_pol" width="24%"></img> <img src="sim_gifs/nip.gif" alt="ni_pol" width="25.5%">

- Physics-Informed Neural Network <br>
<img></img>


### Dependencies: -
1. Python (in PATH)
2. C++ (in PATH)
2. matplotlib
3. NumPy
4. SciPy (for kuramoto)
5. PyTorch and related libraries

(All shell commands are for a windows environment)

```bash
git clone https://github.com/nishantak/Numerical-Sim.git
cd Numerical-Sim
pip install -r requirements.txt
```

- [Transport_Burgers](#transport_burgers-c-code)
- [Kuramoto](#kuramoto-python-code)
- [PINN Kuramoto](#pinn-kuramoto)

## Transport_Burgers C++ Code
**FV_sim.h** and **FV_sim.cpp** constitute A CUSTOM NUMERICAL ANALYSIS LIBRARY that contains _all the functions and scheme implementations._ **simulate.cpp** contains all simulation parameters and the flux definition (f(u)).

```bash
cd cpp_Transport_Burgers
g++ simulate.cpp FV_sim.cpp -o simulate && ./simulate
```

## Kuramoto Python Code
In their *respective directory*, **scheme.py** is the module that contains _the respective numerical analysis scheme implementation._ **functions.py** is the module that contains _functionality functions._ **config.py** contains all simulation parameters and the flux definition (f(u)). Set problem equation and simulation parameters in the **config.py** and **kuramoto_main.py** file
 
```bash
cd python_Kuramoto
python kuramoto_main.py
```

## PINN Kuramoto
Trains a Physics Informed Neural Network with: -
- 4 hidden layers 
- 64 units each 
- tanh activation

Predicts u(x). Check experiments and implementation in the [Notebook](/PINN_Kuramoto/pinn_solver.ipynb)