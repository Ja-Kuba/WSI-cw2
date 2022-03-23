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


g0 = gg.to_np_array(gg.getGraph_complete(10))
g1 = gg.to_np_array(gg.getGraph_bipartite(10))

v1 = VertexCoverSolver(g1)
v1.printPopulation()


#gg.print_graph(g0, 'graph.png')
#gg.print_graph(g1, 'graph1.png')

