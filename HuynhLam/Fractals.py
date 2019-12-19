# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:11:19 2019

@author: huynhlam
"""
#%% INTRODUCTION TO FRACTALS
#Reference: Landau, Páez, Bordeianu, Computational Physics - Problem Solving with Computers (2007)

#It is common in nature to notice objects, called fractals, that do not have well-defined geometric shapes,
#but nevertheless appear regular and pleasing to the eye.
#These objects have dimensions that are fractions, and occur in plants, sea shells, polymers, thin films, colloids, and aerosols.
#We will not study the scientific theories that lead to fractal geometry,
#but rather will look at how some simple models and rules produce fractals.
#To the extent that these models generate structures that look like those in nature,
#it is reasonable to assume that the natural processes must be following similar rules
#arising from the basic physics or biology that creates the objects.

print('========================')
print('INTRODUCTION TO FRACTALS')
print('========================')
print('Fractals do not have well-defined geometric shapes, but nevertheless appear regular and pleasing to the eye.')
print('These objects have dimensions that are fractions, and occur in plants, sea shells, polymers, thin films, colloids, and aerosols.')
print('========================')
print('THE SIERPINSKI GASKET')
print('For the first example, let us look at the Sierpinski gasket')

# import necessary modules
# ------------------------
import numpy as np #math library
from random import randint #random integer generator
import matplotlib.pyplot as plt # Plotting library
from scipy.optimize import curve_fit # Curve fitting

# THE SIERPINSKI GASKET

# In this part, I would like to generate the Sierpinski triangle by drawing dot with some set of rules
# followed by chances determined by randomness
# Then I would like to calculate the fractal dimension of the Sierpinski triangle

# It takes two inputs
# "dim" is the dimension of the grid
# "N" is the number of iterations

def Sierpinski(dim,N):    
    # Create the grid to save the Sierpinski triangle data
    grid = np.zeros((dim,dim))
    # Draw an equilateral triangle on the grid (coordinates of the 3 vertices)
    grid[0,0] = 1
    grid[dim-1,0] = 1
    grid[int((dim-1)/2),int((dim-1)*np.sin(60/180*np.pi))] = 1
    # Place a dot at an arbitrary point P (randomly) within the triangle
    xP = randint(0, dim-1)
    if xP <= (dim-1)/2:
        yP = randint(0, int(xP*np.tan(60/180*np.pi)))
    else:
        yP = randint(0, int(abs(dim-1-xP)*np.tan(60/180*np.pi)))
    grid[xP,yP] = 1
    # Recursive relations to generate Sierpinski triangle
    # Find the next point by selecting randomly the integer 1, 2, or 3
    # (a) If 1, place a dot halfway between P and vertex 1.
    # (b) If 2, place a dot halfway between P and vertex 2.
    # (c) If 3, place a dot halfway between P and vertex 3.
    # Repeat the process, using the last dot as the new P.
    for i in range(N):
        case = randint(1, 3)
        if case == 1:
            grid[int((0+xP)/2),int((0+yP)/2)] = 1
            [xP,yP] = [int((0+xP)/2),int((0+yP)/2)]
        elif case == 2:
            grid[int((dim-1+xP)/2),int((0+yP)/2)] = 1
            [xP,yP] = [int((dim-1+xP)/2),int((0+yP)/2)]
        else:
            grid[int((dim-1+2*xP)/4),int(((dim-1)*np.sin(60/180*np.pi)+yP)/2)] = 1
            [xP,yP] = [int((dim-1+2*xP)/4),int(((dim-1)*np.sin(60/180*np.pi)+yP)/2)]
    
    # This section is to help to determine the fractal dimension later on
    # Mass of the Sierpinski triangle, assume that each dot has mass 1
    mass = sum(sum(grid))
    # Area of the equilateral triangle
    A_Triangle = dim**2*np.sqrt(3)/2
    # Density of the Sierpinski triangle
    rho = mass/A_Triangle
    return grid, rho

# Inputs
N_scal = 10
scaling = np.zeros((N_scal-1,2))

# Generating the Sierpinski triangles with different dimensions to determine the scaling
# And from then figure out the fractal dimensions

print('Generating Sierpinski gaskets with different dimensions')
for i in range(1,N_scal):
    dim = 100*i
    N = 500*1000
    # Generate the Sierpinski triangle
    grid, rho = Sierpinski(dim,N)
    scaling[i-1,:] = [dim,rho]
    print('Gasket number',i,'with side dimension of',dim)
    
print('=========================================')
print('Plotting an example of a Sierpnski gasket')
# Plotting    
plt.figure('Sierpinski')
plt.title('An example of a Sierpinski gasket')
plt.imshow(grid)
plt.text(400, 50, "The fractal was constructed")
plt.text(400, 100, "statistically with 500,000 points.")
plt.text(400, 150, "Each filled part of this figure")
plt.text(400, 200, "is self-similar.")
print('Plotting the scaling law')
plt.figure('Scaling')
plt.title('Scaling law and dimension for Sierpinski gasket')
plt.xlabel('Length of the triangle side: L')
plt.ylabel('Density of the Sierpinski triangle: rho')
plt.plot(scaling[:,1],scaling[:,0],'o', label="Data")

print('Doing a fit to density as function of gasket size using scaling law to figure out the fractal dimension')
def fit(x, amp, d):
    return amp*x**(d-2)
init_vals = [1, 1]  # for [amp, cen, wid]
best_vals, covar = curve_fit(fit, scaling[:,0], scaling[:,1], p0=init_vals)
plt.figure('Scaling')
plt.plot(best_vals[0]*scaling[:,0]**(best_vals[1]-2),scaling[:,0], label=r'Fit with $\rho = C.L^{d - 2}$')
#plt.text(0.185, 700, "The dimention is"+str(best_vals[1]))
plt.text(0.18, 700, "The fractal dimention is d = %.2f" %best_vals[1])
plt.legend()
print("The fractal dimention is d = %.2f" %best_vals[1])

#==================================================================================================================
# BEAUTIFUL BARNSLEY'S FERN
#==================================================================================================================
#It seems paradoxical that natural processes subject to chance can produce objects of high regularity and symmetry.
#For example, it is hard to believe that something as beautiful and symmetric as a fern has random elements in it.
#Nonetheless, there is a clue here in that much of the fern’s beauty arises from the similarity
#of each part to the whole (self-similarity), with different ferns similar, but not identical, to each other.
#These are characteristics of fractals.
#Your problem is to discover if a simple algorithm including some randomness can draw regular ferns.
#If the algorithm produces objects that resemble ferns, then presumably you have uncovered mathematics similar to
#that responsible for the shape of ferns.

print('=========================================')
print('BEAUTIFUL BARNSLEY\'S FERN')
print('It seems paradoxical that natural processes subject to chance can produce objects of high regularity and symmetry.')
print('For example, it is hard to believe that something as beautiful and symmetric as a fern has random elements in it.')
print('In this section, we would like to discover if a simple algorithm including some randomness can draw regular ferns.')
print('If the algorithm produces objects that resemble ferns, then presumably you have uncovered mathematics similar to that responsible for the shape of ferns.')
print('=========================================')

#===================================================================================================================
# Number of iterations
N = 30000
# Initial point
xn = 0.5
yn = 0.0

def fern(N,xn,yn):    
    # Create an array to save points that we will generate randomly
    grid = np.zeros((2,N))
    # First point
    grid[:,0] = [xn,yn]
    # Recursive relation
    # There are four cases with certain probability
    # Grow up, grow left, grow right and turn leaves
    # We can play with the number to grow different ferns
    for i in range(1,N):
        case = np.random.choice([1,2,3,4], p=[0.01, 0.15, 0.14, 0.7])
        if case == 1:
            xn = 0.5
            yn = 0.15*yn
        elif case == 2:
            xn = -0.139*xn + 0.263*yn + 0.57
            yn = -0.246*xn + 0.3*yn - 0.036
        elif case == 3:
            xn = 0.17*xn - 0.215*yn + 0.408
            yn = 0.222*xn + 0.4*yn + 0.0893
        else:
            xn = 0.88*xn + 0.034*yn + 0.1075
            yn = -0.032*xn + 0.88*yn + 0.27
        grid[:,i] = [xn,yn]
    return grid

print('Generating an example of a fern')
fern_grid = fern(N,xn,yn)
print('Plotting the fern')
plt.figure('Fern')
plt.scatter(fern_grid[0,:],fern_grid[1,:], s=0.01, color = 'green')
plt.title('An example of a fern generated statistically with %.0f iterations' %N)

#==================================================================================================================
# FRACTAL TREE
#==================================================================================================================

print('=========================================')
print('FRACTAL TREE')
print('Here is another example where we will generate a tree with fractal dimension using randomness and recursive relation')
print('=========================================')

# Number of iterations
N = 100000
# Initial point
xn = 0.1
yn = 0.1

def Fractal_tree(N,xn,yn):    
    # Create an array to save points that we will generate randomly
    grid = np.zeros((2,N))
    # First point
    grid[:,0] = [xn,yn]
    # Recursive relation
    # There are six cases with certain probability
    # We can play with the number to grow different trees
    for i in range(1,N):
        case = np.random.choice([1,2,3,4,5,6], p=[0.1, 0.1, 0.2, 0.2, 0.2, 0.2])
        if case == 1:
            xn = 0.05*xn
            yn = 0.6*yn
        elif case == 2:
            xn = 0.05*xn
            yn = -0.5*yn + 1.0
        elif case == 3:
            xn = 0.46*xn - 0.15*yn
            yn = 0.39*xn + 0.38*yn + 0.6
        elif case == 4:
            xn = 0.47*xn - 0.15*yn
            yn = 0.17*xn + 0.42*yn + 1.1
        elif case == 5:
            xn = 0.43*xn + 0.28*yn
            yn = -0.25*xn + 0.45*yn + 1.0
        else:
            xn = 0.43*xn + 0.28*yn
            yn =-0.35*xn + 0.31*yn + 0.7
        grid[:,i] = [xn,yn]
    return grid

print('Generating the tree')
tree_grid = Fractal_tree(N,xn,yn)

print('Plotting the tree')
plt.figure('Fractal tree')
plt.title('An example of a fractal tree generated statistically with %.0f iterations' %N)
plt.style.use('seaborn-whitegrid')
rng = np.random.RandomState(0)
colors = rng.rand(N)
sizes = rng.rand(N)
plt.scatter(tree_grid[0,:],tree_grid[1,:], c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar();