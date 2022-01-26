from extract_data import *
from utility import *
import copy
import matplotlib.pyplot as plt


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
    p = 0.005
    if t == t0:
        return rand(p)
    elif t == t0+1:
        return rand(0.75*p)
    elif t == t0+2:
        return rand(0.5*p)
    else:
        return rand(p**(t-t0))


def like_condition(t, t0):
    p = 0.02
    if t == t0:
        return rand(p)
    elif t == t0+1:
        return rand(0.75*p)
    elif t == t0+2:
        return rand(0.5*p)
    else:
        return rand(p**(t-t0))


def propagation(vertex, edges, strategie, time):
    """prend en entrée un graph vertex edges et strategie et effectue le propagation sur ce graph

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
        strategie (list): liste des user_id qui post en premier
        time (int) : nombre d'itération effectuée de propagation
    """
    nb_like = []
    nb_personne_like = []
    nb_personne_repost = []
    tps = [0]

    like = {}  # clé user_id: value:[user_id]
    post = set()  # user_id des gens qui ont posté
    time_post = {}  # clé user_id value: iteration t de l'ajout de user à pot
    for elt in strategie:
        post.add(elt)
        time_post[elt] = 0

    nb_like.append(len(strategie))
    nb_personne_like.append(len(strategie))
    nb_personne_repost.append(len(strategie))

    for i in range(1, time):
        post_2 = copy.deepcopy(post)
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

        # compte le nombre de like total:
        count = 0
        for y in like:
            count += len(like[y])

        tps.append(i)
        nb_personne_like.append(len(like.keys()))
        nb_like.append(count)
        nb_personne_repost.append(len(post))

    return tps, nb_like, nb_personne_like, nb_personne_repost
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(tps, nb_like, 'tab:green')
    axs[0, 0].plot(tps, var(nb_like), 'tab:orange')
    axs[0, 0].set_title('Nombre de like en fonction du temps')

    axs[0, 1].plot(tps, nb_personne_like, 'tab:green')
    axs[0, 1].plot(tps, var(nb_personne_like), 'tab:orange')
    axs[0, 1].set_title('Nombre de personne qui like')

    axs[1, 0].plot(tps, nb_personne_repost, 'tab:green')
    axs[1, 0].plot(tps, var(nb_personne_repost), 'tab:orange')
    axs[1, 0].set_title('Nombre de personne qui repost')
    plt.show()
