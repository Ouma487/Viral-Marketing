from utility import get_keys_to_list, adj_list
import igraph as ig
import matplotlib.pyplot as plt


def afficher_graph(vertex, edges):
    """Affiche le graph

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
    """
    lst = adj_list(vertex, edges)
    g = ig.Graph(edges=lst, directed=True)
    print("en cours")
    g.vs['label'] = get_keys_to_list(vertex)
    ig.plot(g)
    plt.show()
