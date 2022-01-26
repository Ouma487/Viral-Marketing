from extract_data import *
from utility import *

alpha = 0  # proba de liker
beta = 0  # propa de repost


def propagation(vertex, edges, strategie, time):
    """prend en entrée un graph vertex edges et strategie et effectue le propagation sur ce graph

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
        strategie (list): liste des user_id qui post en premier
        time (int) : nombre d'itération effectuée de propagation
    """
    like = [0 for i in range(0, len(df_accounts))]
    post = [0 for i in range(0, len(df_accounts))]
    for elt in strategie:
        k = vertex[elt]
        post[k] += 1
    lst = adj_list(vertex, edges)
    g = ig.Graph(edges=lst, directed=True)
    for i in range(0, time):
        pass

    raise NotImplemented
