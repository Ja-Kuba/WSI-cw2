from math import ceil
import networkx as nx
import matplotlib.pyplot as plt
import random
from itertools import combinations, groupby

class GraphGenerator:
    def __init__(self) -> None:
        pass

    @classmethod
    def getGraph_complete(cls, size:int):
        graph = nx.complete_graph(size)

        return graph

    @classmethod
    def getGraph_bipartite (cls, size:int):
        sr = int(ceil(size/2))
        sl = size - sr
        graph = nx.complete_bipartite_graph(sr, sl)

        return graph

    #TO DO...
    @classmethod
    def getGraph_random(cls, size:int):
        graph = nx.complete_graph(size)

        return graph
    
    @classmethod
    def gnp_random_connected_graph(cls, n, p):
        if p <= 0 or p >1: 
            raise ValueError(f"p= {p} out of range (0,1] ")
        edges = combinations(range(n), 2)
        G = nx.Graph()
        G.add_nodes_from(range(n))
        
        for _, node_edges in groupby(edges, key=lambda x: x[0]):
            node_edges = list(node_edges)
            random_edge = random.choice(node_edges)
            G.add_edge(*random_edge)
            for e in node_edges:
                if random.random() > p:
                    G.add_edge(*e)
        return G
    

    @classmethod
    def to_np_array(cls, graph):
        return nx.convert_matrix.to_numpy_array(graph)

    @classmethod
    def print_graph(cls, graph, filepath, marked=[]):
        color_map = []
        for i, node in enumerate(graph):
            if i < len(marked) and marked[i] == 1:
                color_map.append('red') 
            else:
                color_map.append('green') 
            
        nx.draw(graph, node_color = color_map,
                node_size = 800,
                with_labels=True,
                edge_color ='black',
                width=2
        )
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        #plt.show()


    
if __name__ == "__main__":
    gg = GraphGenerator()
    
    g1 = gg.gnp_random_connected_graph(10, 0.6)
    gg.print_graph(g1, 'graph.png', [1,1,0,0,1])