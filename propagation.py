from numpy import true_divide
from extract_data import *
from utility import *
import copy

alpha = 0  # proba de liker
beta = 0  # propa de repost


def voisin(x, lst):
    """renvoie la liste des voisins de x

    Args:
        x (int): numéro du noeud 
        lst (lst): liste d'adjacence

    Returns:
        lst: liste des voisins de x
    """
    voisin = []
    for elt in lst:
        if elt[1] == x:
            voisin.append(elt[0])
    return voisin


def condition(str, i, j):
    return True


def propagation(vertex, edges, strategie, time):
    """prend en entrée un graph vertex edges et strategie et effectue le propagation sur ce graph

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
        strategie (list): liste des user_id qui post en premier
        time (int) : nombre d'itération effectuée de propagation
    """
    like = {}
    post = set()
    time_post = {}
    for elt in strategie:
        post.add(elt)
        time_post[elt] = 0
    lst = adj_list(vertex, edges)
    for i in range(1, time):
        post_2 = copy.deepcopy(post)
        for x in post_2:
            for y in voisin(vertex[x], lst):
                if y in post:
                    continue
                if condition("repost", i, time_post[x]):
                    if y in like:
                        like[y].append(x)
                    else:
                        like[y] = [x]
                    post.add(y)
                    time_post[y] = i
                elif y in like:
                    pass
                elif condition("like", i, time_post[x]):
                    if y in like:
                        like[y].append(x)
                    else:
                        like[y] = [x]
                else:
                    pass
    return post, like
