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


def repost_condition(i, j):
    return rand(0.005)


def like_condition(i, j):
    return rand(0.01)


def propagation(vertex, edges, strategie, time):
    """prend en entrée un graph vertex edges et strategie et effectue le propagation sur ce graph

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
        strategie (list): liste des user_id qui post en premier
        time (int) : nombre d'itération effectuée de propagation
    """
    like = {}  # clé user_id: value:[user_id]
    post = set()  # user_id des gens qui ont posté
    time_post = {}  # clé user_id value: iteration t de l'ajout de user à pot
    for elt in strategie:
        post.add(elt)
        time_post[elt] = 0
    for i in range(1, time):

        # compte le nombre de like total:
        count = 0
        for y in like:
            count += len(like[y])
        print(count)

        post_2 = copy.deepcopy(post)
        for x in post_2:
            for y in edges[x]:
                if y in post:
                    continue
                # On n'a pas reposté l'information
                if repost_condition(i, time_post[x]):
                    if y in like:
                        like[y].append(x)
                    else:
                        like[y] = [x]
                    post.add(y)
                    time_post[y] = i

                # Si on ne reposte pas
                elif like_condition(i, time_post[x]):
                    if y in like:
                        like[y].append(x)
                    else:
                        like[y] = [x]
    return post, like
