from math import ceil
import networkx as nx
import matplotlib.pyplot as plt



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
    def to_np_array(cls, graph):
        return nx.convert_matrix.to_numpy_array(graph)

    @classmethod
    def print_graph(cls, graph, filepath):
        nx.draw(graph, node_color = 'green', node_size = 1500)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.show()