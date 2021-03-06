# -*- coding: utf-8 -*-
"""
Plots the 2D Brownian motion of particles in a grid of size 100, where the
particles are free to move up, down, left, and right within the bounds and 
become stuck to adjacent boundaries and particles.

Created on Wed Nov 21 10:10:20 2018
@author: Pierino Zindel
"""
#import libraries
import numpy as np
import pylab as plt
from time import time
from random import randint, seed

#parameters of our problem
L = 101 #grid length
N = 100 #number of particles
#frames of the animation to skip
skip = 20

#function that randomly moves the particle and returns the coordinates
def move(i,j):
    #generate a random number corresponding to a direction
    n = randint(1,4)
    #move the position using the random number
    if n == 1:
        i += 1
    elif n == 2:
        i -= 1
    elif n == 3:
        j += 1
    elif n == 4:
        j -= 1
    else:
        raise Exception("invalid move for particle; random value outside of \
                        range")
    return i,j

#function to check the boundary and returns turn if the particle becomes stuck
def stuck_check(i,j,particles):
    #check for the boundary
    if i  == 0 or j == 0 or i == (L-1) or j == (L-1):
        return True
    #check for surrounding particles
    for particle in particles:
        if i == (particle[0]+1) and j == particle[1]:
            return True
        elif i == (particle[0]-1) and j == particle[1]:
            return True
        elif i == particle[0] and j == (particle[1]+1):
            return True
        elif i == particle[0] and j == (particle[1]-1):
            return True
    return False

#function that plots position of particle at x,y and all stuck particles
def plot_traj(x,y,traj,save):
    plt.figure()
    plt.title("2D Brownian Motion Simulation")
    plt.ylabel("y position")
    plt.xlabel("x position")
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.plot(x,y,'.',c='red')
    coord = np.array(traj)
    if len(traj) > 0: plt.plot(coord[:,0], coord[:,1], '.',c='blue')
    plt.grid()
    if save:
        plt.savefig("../images/brownian_trajectories_n=100.png", dpi=500)
    plt.show()

#container for positions of all stuck particles
particles = []
#container for the trajectories of all particles
trajectories = []
#bool to quit the program when the starting point is stuck
quit_loop = False
#seed the random generator
seed(time())

#loop over each particle
for k in range(N):
    #set starting position
    i = L//2
    j = L//2
    #containers for the particles trajectory
    x = [i]
    y = [j]
    #tracking varibles for terminating the program when done
    stuck = False
    step_count = 0
    
    #update particles trajectory until it becomes stuck
    while not stuck:
        #move the position
        i,j = move(i,j)
        step_count += 1
        #store the coordinates
        x.append(i)
        y.append(j)
        #check if the particle is done moving
        stuck = stuck_check(i,j,np.array(particles))
       #terminate loop if stuck particles have reached starting position 
        if stuck and step_count < 2:
            quit_loop = True
            break
        #plot the steps for every tenth frame
        if step_count % skip == 0:
            plot_traj(i,j,particles,False)
        
    #store the final coordinates of the particle
    particles.append([i,j])
    #terminate loop if stuck particles have reached starting position
    if quit_loop: break

#plot final positions of all particles and save the figure
plot_traj(i,j,particles, False)

