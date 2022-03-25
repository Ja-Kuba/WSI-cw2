# @author jkowalczuk 03/2022
from glob import glob1
import random
import numpy as np

import networkx as nx
from graph_generator import GraphGenerator as gg
from vertex_cover_solver import VertexCoverSolver, Stats
from time import perf_counter_ns


def process_results(statistics:list[Stats], times:list[float])->None:
    for s in statistics:
        pass
    pass


def test(g, p, force, p_size, iter_cnt=700) -> None:
    v1 = VertexCoverSolver(g)
    statistics = []
    times = []
    for i in range(RUNS_CNT):
        print(f"run test {i}:")
        print(f"p_mut: {p}\nforce={force}")
        start_t = perf_counter_ns()
        #solve graph
        stats = v1.solve(iter_cnt=iter_cnt, p_size=p_size, p_mutation=p, mutation_force=force)
        statistics.append(stats)
        #get times
        end_t = round((perf_counter_ns() - start_t)/1e6, 2)
        times.append(end_t)
        
        print(f"time: {end_t}[ms]")
        print(f"-------------")
    
    process_results(stats, times)


SEED=9
RUNS_CNT = 2
GRAPH_SIZE = 6
#init randoms
np.random.seed(SEED)
random.seed(SEED)

#generate test graphs
gg0 = gg.getGraph_complete(GRAPH_SIZE)
gg1 = gg.getGraph_bipartite(GRAPH_SIZE)
gg2 = gg.gnp_random_connected_graph(GRAPH_SIZE, 0.6)

#conver graphs to adjacency matrix 
g0 = gg.to_np_array(gg0)
g1 = gg.to_np_array(gg1)
g2 = gg.to_np_array(gg2)

#sample random solution
v2 = VertexCoverSolver(g0)
stats = v2.solve(iter_cnt=500, p_size=400, p_mutation=0.03, mutation_force=2)
gg.print_graph(gg2, 'graph_comp_res.png', stats.result)

#sample random solution
v2 = VertexCoverSolver(g1)
stats = v2.solve(iter_cnt=500, p_size=400, p_mutation=0.03, mutation_force=2)
gg.print_graph(gg2, 'graph_bi_res.png', stats.result)

#sample random solution
v2 = VertexCoverSolver(g2)
stats = v2.solve(iter_cnt=500, p_size=400, p_mutation=0.03, mutation_force=2)
gg.print_graph(gg2, 'graph_ran_res.png', stats.result)

input("cont?")


#start tests
probs = [0.03, 0.08, 0.1, 0.6]

print("//-*-*-*-*//start random//-*-*-*-*//")
for p in probs:
    test(g2, p=p, force=2, p_size=400, iter_cnt=500)

print("start complete")
print("//-*-*-*-*//start complete//-*-*-*-*//")
for p in probs:
    test(g0, p=p, force=2, p_size=400, iter_cnt=500)

print("//-*-*-*-*//start bipartite//-*-*-*-*//")
for p in probs:
    test(g1, p=p, force=2, p_size=500)





