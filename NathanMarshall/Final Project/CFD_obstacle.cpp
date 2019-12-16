#include <fstream>
#define grid 50
using namespace std;

int main() {
    //create variables
    //note: I will be using indices for 2d arrays as [x][y]
    double sf[grid][grid], v[grid][grid]; //stream function,  vorticity
    double dv[grid][grid]; //vorticity time derivative
    int bounds[grid][grid]; //holds boundaries of the obstacle
    double Re, dx, dy, dt, beta;
    int numstp, numitr, stp, itr;
    Re = 50.0;
    dx = 1.0/(grid-1);
    dy = 1.0/(grid-1);
    dt = 0.001;
    numstp = 1200;
    numitr = 100;
    stp = 0;
    itr = 0;
    beta = 1.5;
    ofstream file("CFD_obstacle2.bin", ios::out|ios::binary);

    //set initial value for all arrays to zero

    for(int i=0; i < grid; i++){
        for(int j=0; j < grid; j++){
            sf[i][j] = 0.0;
        }
    }

    for(int i=0; i < grid; i++){
        for(int j=0; j < grid; j++){
            v[i][j] = 0.0;
        }
    }

    for(int i=0; i < grid; i++){
        for(int j=0; j < grid; j++){
            dv[i][j] = 0.0;
        }
    }

    //set obstacle region
    for(int i=0; i < grid; i++){
        for(int j=0; j < grid; j++){

            if ((21 <= i) & (i <= 29) & (21 <= j) & (j <= 29)){
                bounds[i][j] = 1;
            }
            else{
                bounds[i][j] = 0;
            }
        }
    }
    
    while(stp < numstp){

        //solve Poisson eqn. for stream function
        itr = 0;
        while(itr < numitr){

            for(int i=1; i < grid-1; i++){
                for(int j=1; j < grid-1; j++){
                    if (bounds[i][j] == 1){
                        continue;
                    }
                    else{
                        sf[i][j] = 0.25*beta*(sf[i+1][j]+sf[i-1][j]+sf[i][j+1]+sf[i][j-1]
                                   +v[i][j]*dx*dx)+(1.0-beta)*sf[i][j];
                    }
                }
            }
            itr++;
        }

        //set boundaries for vorticity

        for(int i=0; i < grid; i++){
            for(int j=0; j < grid; j++){
                if(bounds[i][j] == 1){
                    v[i][21] = -2.0 * (sf[i][20])/dy/dy; //set the boundaries for the obstacle
                    v[i][29] = -2.0 * (sf[i][30])/dy/dy;
                    v[21][j] = -2.0 * (sf[20][j])/dx/dx;
                    v[29][j] = -2.0 * (sf[30][j])/dx/dx;
                }
                else{
                    v[i][0] = -2.0 * (sf[i][1])/dy/dy; //left wall
                    v[i][grid-1] = -2.0 * (sf[i][grid-2])/dy/dy; //right wall
                    v[0][j] = -2.0 * (sf[1][j])/dx/dx; //bottom wall
                    v[grid-1][j] = -2.0 * (sf[grid-2][j])/dx/dx - 2.0/dx; //top wall
                }
            }
        }

        //calculate vorticity time derivative with transport eqn

        for(int i=1; i < grid-1; i++){
            for(int j=1; j < grid-1; j++){
                dv[i][j] =  -0.25*((sf[i][j+1] - sf[i][j-1])*(v[i+1][j] - v[i-1][j])
                            - (sf[i+1][j] - sf[i-1][j])*(v[i][j+1] - v[i][j-1]))/dx/dx
                            + 1.0/Re * (v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1]-4.0*v[i][j])/dx/dx;
            }
        }

        //update vorticity

        for(int i=1; i < grid-1; i++){
            for(int j=1; j < grid-1; j++){
                v[i][j] +=  dv[i][j] * dt;
            }
        }
        
        stp++;
    }

    //write data to binary file to plot in python
    for(int i=0; i < grid; i++){
        for(int j=0; j < grid; j++){
            file.write((char*)&sf[i][j], sizeof(double));
        }
    }  
    file.close();
    
    return 0;
}