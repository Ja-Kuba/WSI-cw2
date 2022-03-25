# @author jkowalczuk 03/2022
from glob import glob1
import random
import numpy as np

import networkx as nx
from graph_generator import GraphGenerator as gg
from vertex_cover_solver import VertexCoverSolver, Stats
from time import perf_counter_ns
import json



def process_results(statistics:list[Stats], times:list[float])->None:
    b_scores = []
    b_iters = []
    for s in statistics:
        b_scores.append(s.best_score)
        b_iters.append(s.best_iter_found)
        return {
            "b_scores_mean" : np.mean(b_scores),
            "b_iters_mean" : np.mean(b_iters),
            "b_scores_std" : np.std(b_scores),
            "b_iters_std" : np.std(b_iters),
        }


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
    
    return process_results(stats, times)


SEED=9
RUNS_CNT = 10
GRAPH_SIZE = 25
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

##sample random solution
#v2 = VertexCoverSolver(g0)
#stats = v2.solve(iter_cnt=500, p_size=400, p_mutation=0.03, mutation_force=2)
#gg.print_graph(gg2, 'graph_comp_res.png', stats.result)
#
##sample random solution
#v2 = VertexCoverSolver(g1)
#stats = v2.solve(iter_cnt=500, p_size=400, p_mutation=0.03, mutation_force=2)
#gg.print_graph(gg2, 'graph_bi_res.png', stats.result)
#
##sample random solution
#v2 = VertexCoverSolver(g2)
#stats = v2.solve(iter_cnt=500, p_size=400, p_mutation=0.03, mutation_force=2)
#gg.print_graph(gg2, 'graph_ran_res.png', stats.result)
#
#input("cont?")


#start tests
probs = [0.03, 0.08, 0.1, 0.6]

res_random = []
res_complete = []
res_bipartite = []
print("//-*-*-*-*//start random//-*-*-*-*//")
for p in probs:
    tmp_res= test(g2, p=p, force=2, p_size=400, iter_cnt=500)
    print(tmp_res)
    res_random.append(tmp_res)

print("start complete")
print("//-*-*-*-*//start complete//-*-*-*-*//")
for p in probs:
    tmp_res = test(g0, p=p, force=2, p_size=400, iter_cnt=500)
    print(tmp_res)
    res_complete.append(tmp_res)

print("//-*-*-*-*//start bipartite//-*-*-*-*//")
for p in probs:
    tmp_res = test(g1, p=p, force=2, p_size=400, iter_cnt=500)
    print(tmp_res)
    res_bipartite.append(tmp_res)


results_all = {
    "random": res_random,
    "complete": res_complete,
    "bipartite": res_bipartite,
}

j = json.dumps(results_all)
with open("results_prob_p400_i500.json", "w", "utf-8") as f:
    f.write(j)



    





