from cmath import inf
from igraph import Graph
from extract_data import nb_follow, graph


def graphe_aléatoire_powerlaw(n_nodes):
    graphe_aléatoire = Graph.Static_Power_Law(
        n=n_nodes, m=488325, exponent_out=4, exponent_in=inf, loops=True, multiple=False)
    vertex = graph()[0]
    edges = {}
    adj_list = graphe_aléatoire.get_adjlist()
    for v in vertex.keys():
        edges[v] = adj_list[vertex[v]]
    return vertex, edges
