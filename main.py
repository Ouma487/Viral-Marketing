import igraph as ig
import matplotlib.pyplot as plt
from extract_data import *
from utility import *
from extract_data import *
from affichage import *
from plot import *
from strategie import *


def main():
    vertex, edges = graph()
    best_influenceurs(vertex, edges, 0.01)
    """vertex = {14215: 0, 14216: 1, 14235: 2, 14555: 3}
    edges = {14215: [14216, 14555], 14216: [
        14235, 14215], 14235: [14215, 14555]}"""
    #new_vertex, new_edges = degree_min(vertex, edges, 150)
    #afficher_graph(vertex, edges)
    #afficher_graph(new_vertex, new_edges)
    pass


if __name__ == '__main__':
    main()
    # plot_like_time()
