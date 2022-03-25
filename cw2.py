#macierz sąsiedztwa 

#algorytm genetyczny 

#populacja -> zbiór genomów
#turniejowa k = 2
#
from glob import glob1
import random
import numpy as np

import networkx as nx
from graph_generator import GraphGenerator as gg
from vertex_cover_solver import VertexCoverSolver
from time import perf_counter_ns

def test(g, p, force, p_size, iter_cnt=700):
    v1 = VertexCoverSolver(g)
    for i in range(RUNS_CNT):
        print(f"run test {i}:")
        print(f"p_mut: {p}\nforce={force}")
        start_t = perf_counter_ns()
        stats = v1.solve(iter_cnt=iter_cnt, p_size=p_size, p_mutation=p, mutation_force=force)
        end_t = round((perf_counter_ns() - start_t)/1e6, 2)
        print(f"time: {end_t}[ms]")
        print(f"-------------")


SEED=9
RUNS_CNT = 2
GRAPH_SIZE = 25
probs = [0.03, 0.08, 0.1, 0.6]

np.random.seed(SEED)
random.seed(SEED)

gg0 = gg.getGraph_complete(GRAPH_SIZE)
gg1 = gg.getGraph_bipartite(GRAPH_SIZE)
gg2 = gg.gnp_random_connected_graph(GRAPH_SIZE, 0.6)
#gg.print_graph(gg0, 'graph.png')
gg.print_graph(gg2, 'graph_random.png')


g0 = gg.to_np_array(gg0)
g1 = gg.to_np_array(gg1)
g2 = gg.to_np_array(gg2)

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






#gg.print_graph(g0, 'graph.png')
#gg.print_graph(g1, 'graph1.png')
