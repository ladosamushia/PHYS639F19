#include <iostream>
#include <fstream>
#include <cmath>
#define gridx 128
#define gridy 128
using namespace std;

int main(){
    double u[gridx][gridy+1], v[gridx+1][gridy], p[gridx+1][gridy+1];
    double un[gridx][gridy+1], vn[gridx+1][gridy], pn[gridx+1][gridy+1];
    double uc[gridx][gridy], vc[gridx][gridy], pc[gridx][gridy];
    double m[gridx+1][gridy+1];
    double Re, dx, dy, dt, delta, error;
    int numstp, stp;
    Re = 100.0;
    dx = 1.0/(gridx-1);
    dy = 1.0/(gridy-1);
    dt = 0.001;
    delta = 4.5;
    stp = 0;
    error = 1.0;
    ofstream file("CFDstag.bin", ios::out|ios::binary);

    //initialize the u velocity
    for(int i=0; i < gridx; i++){
        for(int j=0; j < gridy+1; j++){
            u[i][j] = 0.0;
            u[i][gridy] = 1.0;
            u[i][gridy-1] = 1.0;
        }
    }   

    //initialize the v velocity
    for(int i=0; i < gridx+1; i++){
        for(int j=0; j < gridy; j++){
            v[i][j]= 0.0;
        }
    }

    //initialize the pressure array
     for(int i=0; i < gridx+1; i++){
        for(int j=0; j < gridy+1; j++){
            p[i][j] = 1.0;
        }
    }
    while(error > 0.0000001){
    //calculate u velocity at next time step
    for (int i=1; i < gridx-1; i++){
			for (int j=1; j < gridy; j++){
				un[i][j] = u[i][j] - dt*(  (u[i+1][j]*u[i+1][j]-u[i-1][j]*u[i-1][j])/2.0/dx 
							+0.25*( (u[i][j]+u[i][j+1])*(v[i][j]+v[i+1][j])-(u[i][j]+u[i][j-1])*(v[i+1][j-1]+v[i][j-1]) )/dy  )
								- dt/dx*(p[i+1][j]-p[i][j]) 
									+ dt*1.0/Re*( (u[i+1][j]-2.0*u[i][j]+u[i-1][j])/dx/dx +(u[i][j+1]-2.0*u[i][j]+u[i][j-1])/dy/dy );
                if (un[i][j] != un[i][j]){
                    cout << "nan at un" << endl;
                    break;
                }
			}
	}

    //boundary conditions 
   for (int j=1; j<=(gridy-1); j++)
		{
			un[0][j] = 0.0;
			un[gridx-1][j] = 0.0;
		}
		
		for (int i=0; i<=(gridx-1); i++)
		{
			un[i][0] = -un[i][1];
			un[i][gridy] = 2 - un[i][gridy-1];
		}
    //calculate v velocity at next time step
    for(int i=1; i < gridx; i++){
        for(int j=1; j < gridy-1; j++){
            vn[i][j] = v[i][j] - dt* (( 0.25*( (u[i][j]+u[i][j+1])*(v[i][j]+v[i+1][j])-(u[i-1][j]+u[i-1][j+1])*(v[i][j]+v[i-1][j]) )/dx 
							+(v[i][j+1]*v[i][j+1]-v[i][j-1]*v[i][j-1])/2.0/dy ) 
								- dt/dy*(p[i][j+1]-p[i][j]) 
									+ dt*1.0/Re*( (v[i+1][j]-2.0*v[i][j]+v[i-1][j])/dx/dx+(v[i][j+1]-2.0*v[i][j]+v[i][j-1])/dy/dy));
			if (vn[i][j] != vn[i][j]){
                    cout << "nan at vn" << endl;
                    break;
                }
            }
	}
        
    //boundary conditions 
   for (int j=1; j<=(gridy-2); j++)
		{
			vn[0][j] = -vn[1][j];
			vn[gridx][j] = -vn[gridx-1][j];
		}		

	for (int i=0; i<=(gridx); i++)
		{
			vn[i][0] = 0.0;
			vn[i][gridy-1] = 0.0;
		}	

    // Solves continuity equation
	for (int i=1; i < gridx; i++){
			for (int j=1; j < gridy; j++){
				pn[i][j] = p[i][j]-dt*delta*(  ( un[i][j]-un[i-1][j] )/dx + ( vn[i][j]-vn[i][j-1] ) /dy  );
                
                if (pn[i][j] != pn[i][j]){
                    cout << "nan at pn" << endl;
                    break;
                }
            }
	}

    //pressure boundary conditions

    for(int i=1; i < gridx; i++){
        pn[i][0] = pn[i][1];
        pn[i][gridy] = pn[i][gridy-1];
    }

    for(int j=0; j < gridy+1; j++){
        pn[0][j] = pn[1][j];
        pn[gridx][j] = pn[gridx-1][j];
    }

    //displaying the error
    error = 0.0;
    for(int i=1; i < gridx; i++){
        for(int j=1; j < gridy; j++){
            m[i][j] = ((un[i][j]-un[i-1][j])/dx + (vn[i][j]-vn[i][j-1])/dy);
            error += abs(m[i][j]);
        }
    }

    if(stp%1000 == 0){
        cout << "Error is " << error << " for step " << stp << endl;
    }

    //iterate u
    for(int i=0; i < gridx; i++){
        for(int j=0; j < gridy+1; j++){
            u[i][j] = un[i][j];
        }
    }   

    //iterate v
    for(int i=0; i < gridx+1; i++){
        for(int j=0; j < gridy; j++){
            v[i][j] = vn[i][j];
        }
    }

    //iterate p
     for(int i=0; i < gridx+1; i++){
        for(int j=0; j < gridy+1; j++){
            p[i][j] = pn[i][j];
        }
    }
    stp++;
    }
    cout << stp;
    cout << error;
    for (int i=0; i < gridx; i++){
		for (int j=0; j < gridy; j++){	
			uc[i][j] = 0.5*(u[i][j]+u[i][j+1]);
			vc[i][j] = 0.5*(v[i][j]+v[i+1][j]);
			pc[i][j] = 0.25*(p[i][j]+p[i+1][j]+p[i][j+1]+p[i+1][j+1]);
		}
	} 

    //write data to binary file to plot in python
    for(int i=0; i < gridx; i++){
        for(int j=0; j < gridy; j++){
            file.write((char*)&uc[i][j], sizeof(double));
        }
    }  

    for(int i=0; i < gridx; i++){
        for(int j=0; j < gridy; j++){
            file.write((char*)&vc[i][j], sizeof(double));
        }
    }  
    file.close();
    
    return 0;
}