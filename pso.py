# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:15:54 2021

@author: Jonny
"""

import random
import math
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------
def objective_function(x):
    y = 3*(1-x[0])**2*math.exp(-x[0]**2 - (x[1]+1)**2) - 10*(x[0]/5 - x[0]**3 - x[1]**5)*math.exp(-x[0]**2 - x[1]**2) -1/3*math.exp(-(x[0]+1)**2 - x[1]**2);
    return y
  
bounds=[(-3,3),(-3,3)]   # límites superior e inferior de las variables
nv = 2                   # numero de variables
mm = 1                   # si es un problema de minimizacion mm = -1; si es un problema de maximizacion mm = 1
  

particle_size=20        # numero de particulas
iterations=20           # numero maximo de interaciones 
w=0.9                   # inertia constant
c1=1.49                 # cognative constant
c2=1.49                 # social constant

#------------------------------------------------------------------------------    
class Particle:
    def __init__(self,bounds):
        self.particle_position=[]                     # posicion de la particula
        self.particle_velocity=[]                     # velocidad de la particula
        self.local_best_particle_position=[]          # mejor posiicon de l aparticula
        self.fitness_local_best_particle_position = initial_fitness
        self.fitness_particle_position = initial_fitness 

        for i in range(nv):
            self.particle_position.append(random.uniform(bounds[i][0],bounds[i][1]))
            self.particle_velocity.append(random.uniform(-1,1))
            
    def evaluate(self,objective_function):
        self.fitness_particle_position=objective_function(self.particle_position)
        
        if mm == -1:
            if self.fitness_particle_position < self.fitness_local_best_particle_position:
                self.local_best_particle_position=self.particle_position                  # actualizar el mejor local
                self.fitness_local_best_particle_position=self.fitness_particle_position  # actualizar la aptitud de los mejores locales
        if mm == 1:
            if self.fitness_particle_position >  self.fitness_local_best_particle_position:
                self.local_best_particle_position=self.particle_position                  # actualizar el mejor local
                self.fitness_local_best_particle_position=self.fitness_particle_position  # actualizar la aptitud de los mejores locales

    def update_velocity(self,global_best_particle_position):
        for i in range(nv):
            r1=random.random()
            r2=random.random()
  
            cognitive_velocity = c1*r1*(self.local_best_particle_position[i] - self.particle_position[i])
            social_velocity = c2*r2*(global_best_particle_position[i] - self.particle_position[i])
            self.particle_velocity[i] = w*self.particle_velocity[i]+ cognitive_velocity + social_velocity
  
    def update_position(self,bounds):
        for i in range(nv):
            self.particle_position[i]=self.particle_position[i]+self.particle_velocity[i]
  
            # comprobar y reparar para satisfacer los límites superiores
            if self.particle_position[i]>bounds[i][1]:
                self.particle_position[i]=bounds[i][1]
            # comprobar y reparar para satisfacer los límites superiores
            if self.particle_position[i]<bounds[i][0]:
                self.particle_position[i]=bounds[i][0]

                

class PSO():
    def __init__(self,objective_function,bounds,particle_size,iterations):
  
        fitness_global_best_particle_position=initial_fitness
        global_best_particle_position=[]
  
        swarm_particle=[]
        for i in range(particle_size):
            swarm_particle.append(Particle(bounds))
        A=[]
          
        for i in range(iterations):
            for j in range(particle_size):
                swarm_particle[j].evaluate(objective_function)
                
                if mm ==-1:
                    if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:
                        global_best_particle_position = list(swarm_particle[j].particle_position)
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
                if mm ==1:
                    if swarm_particle[j].fitness_particle_position > fitness_global_best_particle_position:
                        global_best_particle_position = list(swarm_particle[j].particle_position)
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)
                        
            for j in range(particle_size):
                swarm_particle[j].update_velocity(global_best_particle_position)
                swarm_particle[j].update_position(bounds)
            
            A.append(fitness_global_best_particle_position)
                    
        print('Solucion optima', global_best_particle_position)
        print('Valor de la funcion objetivo:', fitness_global_best_particle_position)
        print('Proceso evolutivo del valor de la función objetiva')
        plt.plot(A)
            
if mm == -1:
    initial_fitness = float("inf")
if mm == 1:
    initial_fitness = -float("inf")       

                
PSO(objective_function,bounds,particle_size,iterations)
