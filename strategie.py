from utility import get_keys_to_list, rand
from extract_data import get_nb_followers, classement_influenceurs_follow
from propagation import *


def random_post(vertex, edges,  p=0.01, nb=5, cout_follower=0.01):
    """Renvoie une liste des personnes qui vont poster la campagne
    Ici le choix est entièrement aléatoire

    Args:
        vertex (dic): vertex
        edges (liste): edges
        p (float): pourcentage of initial people 
    Return:
        list: listes des id_users
    """
    list_id_users = []
    users_id = get_keys_to_list(vertex)
    for user_id in users_id:
        if rand(p):
            list_id_users.append(user_id)
    return list_id_users


def best_influenceurs(vertex, edges, p=0.01, nb=5, cout_follower=0.01):
    """Renvoie une liste de personnes qui vont poster la campagne
    Ici on choisit les nb plus gros influenceurs

    Args:
        vertex (dic): vertex
        edges (list): edges
        nb (int): nombre d'influenceurs que l'on veut cibler
    Return:
        list: liste des meilleurs influenceurs
        cost: ordre de grandeur du cout que celà peut couter
    """
    influenceurs = classement_influenceurs_follow()[:5]
    cost = 0
    for influenceur in influenceurs:
        cost += get_nb_followers(influenceur)*cout_follower
    return influenceurs


def mean_strategie(vertex, edges, strategie, time, N, p=0.01, nb=5, cout_follower=0.01):
    like, personne_like, repost = np.zeros(N), np.zeros(N), np.zeros(N)
    for i in range(N):
        tps, nb_like, nb_personne_like, nb_personne_repost = propagation(
            vertex, edges, strategie(vertex, edges, p, nb, cout_follower), time)

        like[i] = nb_like[-1]
        personne_like[i] = nb_personne_like[-1]
        repost[i] = nb_personne_repost[1]
    return np.mean(like), np.mean(personne_like), np.mean(repost)


def evaluation_strategie():
    vertex, edges = graph()
    print(mean_strategie(vertex, edges, random_post, time=30, N=75, p=0.001, nb=30))
    print(mean_strategie(vertex, edges, random_post, time=30, N=75, p=0.005, nb=30))

    print(mean_strategie(vertex, edges,
          best_influenceurs, time=30, N=75, p=0.001, nb=5))
    print(mean_strategie(vertex, edges, best_influenceurs,
          time=30, N=75, p=0.001, nb=20))

    #propagation(vertex, edges, best_influenceurs(vertex, edges, 30)[0], 50)
