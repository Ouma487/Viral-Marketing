from cmath import inf
from igraph import Graph
from extract_data import nb_follow, graph


def graphe_aléatoire_powerlaw(n_nodes, m=488325):
    graphe_aléatoire = Graph.Static_Power_Law(
        n=n_nodes, m=m, exponent_out=2.5, exponent_in=inf, loops=False, multiple=False)
    vertex = {}
    edges = {}
    adj_list = graphe_aléatoire.get_adjlist()
    for i in range(n_nodes):
        vertex[i] = i
        edges[i] = adj_list[i]
    return vertex, edges
