from utility import get_keys_to_list, rand
from extract_data import classement_influenceurs, get_nb_followers


def random_post(vertex, p):
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


def best_influenceurs(vertex, edges, nb, cout_follower=0.01):
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
    influenceurs = classement_influenceurs()[:5]
    cost = 0
    for influenceur in influenceurs:
        cost += get_nb_followers(influenceur)*cout_follower
    return influenceurs, cost
