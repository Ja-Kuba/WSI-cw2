'''
 Pseudokod  

P_t = init()
t = 0
ocena(P_t)
while !stop
    Tt = selekcja(Pt)
    Ot = mutacja(Tt)
    ocena(Ot)
    Pt = Ot
    t=t+1  
'''

import numpy as np
import random

class VertexCoverSolver:
    def __init__(self, problem:np.array, p_size:int = 200, rand_obj = np.random) -> None:
        self.problem = problem
        self.rand = rand_obj
        self.population = self.init_population(p_size, self.problem.shape[0])


    def tournament_selection(self):
        new_population = np.array
        pass


    def mutation(self):
        pass


    def init_population(self, p_size, v_size):
        return [self.rand.choice([0, 1], size=v_size) for i in range(p_size)]


    def solve(self):
        pass


    def getPopulation(self):
        return self.population


    def printPopulation(self):
        pop1 = self.getPopulation()
        for i, p in enumerate(pop1):
            print(f"{p}[{i}]")