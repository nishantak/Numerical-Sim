#include<bits/stdc++.h>
using namespace std;

//Function Signatures
void simulate(vector<double>&);
void get_param();
void plot();
void write_data(ofstream&, vector<double>);
double calculate_tv(vector<double>&);
// Function Signatures


// Simulation Parameters
int Nx = 201;      // Number of points
double xmin = 0.0, xmax = 2.0;  // Domain limits
double L = abs(xmax- xmin);   // Domain Length
double dx = L/(Nx-1);  // Cell width

double cfl = 0.5; // Stability Parameter - CFL Number 
double c=1; // Wave Velocity

double dt = cfl * dx / c;     // Time step
double Tf = 2.0;         // Final time / Total Time
int Nt = (int)(Tf/dt);  // No. of time steps


vector<double> U(Nx, 0); // U(x);


// Returns Flux, u^2 / 2
double flux(double u){
    return 0.5*u*u;
};


// Returns Numerical Flux, Numerical Flux Scheme (Lax-Friedrich)
double num_flux(double u, double u_next){
    return 0.5 * (flux(u) + flux(u_next)) - (0.5 / (dt/dx) * (u_next - u));
}


/// @brief initialise with intial condition, U_0(x) = cos(pi*x)
void intialise(vector<double> &u){
    for(int j=0; j<Nx; j++)
        u[j] = sin(M_PI*(xmin + j*dx));
}


//Driver Code 
int main(){
    intialise(U);
    simulate(U);

    get_param();

    cout << "Total Variation: " << calculate_tv(U) << endl;
    
    plot();

    return 0;
}


/// @brief Simulating the time stepping of PDE using Finite Volume Method and Flux Scheme
void simulate(vector<double> &u){
    // Output dump files
    ofstream out_file("simulation_data.txt");
    ofstream fin_file("U_final.txt");

    double t=0; //Current Time
    
    write_data(out_file, U); // Write initial data, Time Step 0
    // Time Stepping Loop
    while(t<=Tf){
        for(int j=3; j<=Nx-2; j++){

            // Numerical Flux
            long double F_j_plus_half = num_flux(u[j], u[j+1]);
            long double F_j_min_half = num_flux(u[j-1], u[j]);
            
            // U_xxx Discretization
            long double third_derivative = (u[j] - 3.0*u[j-1] + 3.0*u[j-2] - u[j-3]) / (dx*dx*dx); 

            // Update using Numerical Scheme
            u[j] -= (dt/dx) * (F_j_plus_half - F_j_min_half) + dt * third_derivative ;
        }
        
        // Boundary Conditions | Periodic Boundary Condition
        u[0] = u[Nx-1] ; // Left Boundary
        u[1] = u[0] ; u[2] = u[1];  
        u[Nx-1] = u[Nx-2]; // Right Boundary

        write_data(out_file, U); // Write Simulation Data for THIS time step

        t+=dt;

    } write_data(fin_file, U); // Write Simulation Data for FINAL time step

out_file.close(); fin_file.close();

}


/// @brief Plots the graph using python matplotlib script
void plot(){
    system("python matplot.py");
}


/// @brief Calculates the TV bound
double calculate_tv(vector<double>& u) {
    double tv_norm = 0.0;
    for (int j = 1; j < Nx; j++) {
        tv_norm += abs(u[j] - u[j - 1]);
    }
    
    return tv_norm;
}


/// @brief write data to file
void write_data(ofstream& filename, vector<double> u){
    for(int i=0; i<Nx; i++)
        filename << u[i] << " ";
    filename << endl;
}


/// @brief Print Simulation Parameters
void get_param(){
    cout << endl << "Number of Spatial Points (Nx): " << Nx << endl;
    cout << "Domain Limits (xmin, xmax): " << xmin << ", " << xmax << endl;
    cout << "Domain Length (L): " << L << endl;
    cout << "Cell Width (dx): " << dx << endl << endl;
    cout << "Stability Parameter (CFL Number): " << cfl << endl << endl;
    cout << "Wave Velocity (c): " << c << endl << endl;
    cout << "Time Step (dt): " << dt << endl;
    cout << "Final Time (Tf): " << Tf << endl;
    cout << "Number of Time Steps (Nt): " << Nt << endl << endl;
}