from extract_data import *
from utility import *
import copy
import math


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


def repost_condition(t, t0):
    p = 0.001
    # p(x=k) = p.(1-p)^(k-1)
    return rand(p*(1-p)**(t-t0))


def like_condition(t, t0):
    p = 0.15
    # p(x=k) = p.(1-p)^(k-1)
    # p(x=k) = 1/lambda * exp(-lambda.x)
    return rand(p*(1-p)**(t-t0))


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
        print('like: '+str(count))

        post_2 = copy.deepcopy(post)
        print(len(post))
        for x in post_2:
            for y in edges[x]:
                if y in post or (y in like and x in like[y]):
                    continue
                # On n'a pas reposté l'information
                if (y not in like or (y in like and len(like[y]) < 3)) and repost_condition(i, time_post[x]):
                    if y not in like:
                        like[y] = [x]
                    elif x not in like[y]:
                        like[y].append(x)
                    post.add(y)
                    time_post[y] = i

                # Si on ne reposte pas
                elif like_condition(i, time_post[x]):
                    if y not in like:
                        like[y] = [x]
                    elif x not in like[y]:
                        like[y].append(x)
    return post, like
