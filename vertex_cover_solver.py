from operator import ne
from re import S
import numpy as np
import random
from tournament_genom import TournamentGenom
from stats import Stats

class VertexCoverSolver:
    def __init__(self, problem:np.array, rand_obj = np.random) -> None:
        self.problem = problem
        self.rand = rand_obj
        self.res_size = self.problem.shape[0]


    def init_population(self, p_size, v_size):
        new_population = []
        for _ in range(p_size):
            g = self.rand.choice([0, 1], size=v_size)
            tg = TournamentGenom(g, rand_obj=self.rand)
            tg.fitProblem(self.problem)
            new_population.append(tg)
        
        return new_population


    def get_winner(self, g1:TournamentGenom, g2:TournamentGenom):
        if g1 > g2: return g1
        else: return g2


    def tournament_selection(self, population, p_size, k_size:int=2):
        new_population = []
        for _ in range(p_size):
            t_pair =  random.choices(population, k = k_size)
            tmp = self.get_winner(t_pair[0], t_pair[1])
            new_obj = TournamentGenom.copy_init(tmp)
            new_population.append(new_obj)

        return new_population


    def checkBest(self, tg1:TournamentGenom, tg2:TournamentGenom):
        if tg1 > tg2: 
            return TournamentGenom.copy_init(tg1)
        else: 
            return TournamentGenom.copy_init(tg2)


    def score_population(self, population:list[TournamentGenom]):
        scores = []
        best = TournamentGenom.copy_init(population[0])
        for p in population:
            best = self.checkBest(best, p)
            scores.append(p.getScore())
        
        #print(f"min_score: {min(scores)}")
        #print(f"population best: {best}")
        return best


    def mutate_population(self, population, mutation_force, p_mutation):
        for p in population:
            p.mutate(mutation_force, p=p_mutation)
            p.fitProblem(self.problem)

    '''
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
    def solve(self, iter_cnt, p_size:int=200, mutation_force:int = 1, p_mutation:float = .3):
        all_populations = []
        population = self.init_population(p_size, self.res_size)
        b_result = self.score_population(population)
        res_found_iter = 0
        for i in range(iter_cnt):
            all_populations.append(population)
            new_population = self.tournament_selection(population, p_size=p_size)
            self.mutate_population(new_population, mutation_force, p_mutation)
            result = self.score_population(new_population)
            population = new_population
            
            if b_result > result: pass
            else:
                b_result = TournamentGenom.copy_init(result)
                res_found_iter = i
            
            # if i%100==0: 
            #     print(f"iter {i}")
            #     print(f"best_genome: {b_result}")


        print(f"best_genome: {b_result}")
        print(f"iter: {res_found_iter}")
        return Stats(
            populations_list = all_populations,
            result = b_result.getGenom(),
            best_iter_found = all_populations
        )

    @classmethod
    def printPopulation(cls, population):
        for i, p in enumerate(population):
            print(f"{p}[{i}]")



if __name__ == "__main__":
    
    #def get_winner(self, g1:TournamentGenom, g2:TournamentGenom):
    #    if g1 > g2: return g1
    #    else: return g2
    
    
    t1 = TournamentGenom(np.array([1,0,0,0]))
    t2 = TournamentGenom(np.array([1,0,0,0]))
    t1.positive_cnt = 2
    t1.uncover_cnt = 0
    t1.combo_score = 0

    t2.positive_cnt = 3
    t2.uncover_cnt = 0
    t2.combo_score = 1

    print(t1 > t2)
    #t1 = TournamentGenom(np.array([1,0,0,0]))
    #t2 = t1
    #print(f"t1: {t1}")
    #print(f"t2: {t2}")
    #t1.uncover_cnt = 10
    #print(f"t1: {t1}")
    #print(f"t2: {t2}")
    
    
    pass
