# ensemble de fonctions avec des propriétés qui peuvent être utiles
import igraph as ig


def adj_list(vertex, edges):
    """Renvoie la liste d'adjacence.
    C'est la même chose que edges mais avec les numéros du graphs (et non les id)

    Args:
        vertex (dic): vertex
        edges (list): liste des edges

    Returns:
        list: liste d'adjacence
    """
    adj = []
    for user_id in edges:
        for follow_id in edges[user_id]:
            adj.append([vertex[user_id], vertex[follow_id]])
    return adj


def get_keys_to_list(dic):
    """Renvoie la liste des cles

    Args:
        dic (dic): un dictionnaire

    Returns:
        list: liste des clés du dictionnaire
    """
    liste = []
    for key in dic:
        liste.append(key)
    return liste


def degree_min(vertex, edges, epsilon):
    """prend en entrée une graph sous la forme d'un couple edge vertex
    et epsilon une valeur arbitraire minimale on enlève les noeuds du 
    graph qui ont un degree qui est inférieur à epsilon

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
        epsilon (int): la valeur de garde
    """
    lst = adj_list(vertex, edges)
    g = ig.Graph(edges=lst, directed=True)
    g.vs["users_id"] = get_keys_to_list(vertex)
    new_vertex = {}
    new_edges = {}
    k = 0
    for elt in g.vs["users_id"]:
        if g.degree(vertex[elt], mode="in") > epsilon:
            new_vertex[elt] = k
            k += 1
    for elt in new_vertex:
        l = []
        if not(elt in edges):
            continue
        for follower in edges[elt]:
            if follower in new_vertex:
                l.append(follower)
        new_edges[elt] = l
    return new_vertex, new_edges


def transform_to_list(l):
    """Passe d'une chaine de caractere en une liste donc de:
    '[1, 2, 3]' -> [1, 2, 3]

    Args:
        l (string): chaine de caractere d'une liste

    Returns:
        list: liste
    """
    j = l[0][1:len(l[0])-1]
    o = []
    k = ""
    for i in range(0, len(j)):
        if j[i] == ",":
            o.append(k)
            k = ""
        elif i == len(j) - 1:
            k += j[i]
            o.append(k)
        elif j[i] == " ":
            continue
        else:
            k += j[i]

    res = []
    for elt in o:
        res.append(int(elt))

    return res
