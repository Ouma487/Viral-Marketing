from utility import get_keys_to_list, adj_list, var
import igraph as ig
import matplotlib.pyplot as plt
from extract_data import classement_influenceurs_follow


def limiter_graph(vertex, edges, N):
    id_infuenceurs = classement_influenceurs_follow()[:N]
    nw_vertex = {}
    nw_edges = {}
    for i in range(N):
        id_inf = id_infuenceurs[i]
        nw_vertex[id_inf] = i
        for id_follow in edges[id_inf]:
            if id_follow in id_infuenceurs:
                if id_inf in nw_edges:
                    nw_edges[id_inf].append(id_follow)
                else:
                    nw_edges[id_inf] = [id_follow]
    return nw_vertex, nw_edges


def afficher_propagation(tps, nb_like, nb_personne_like, nb_personne_repost):
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
    return fig, axs


def afficher_graph(vertex, edges, nom='user', color=False):
    """Affiche le graph

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
        nom : user ou nb
    """
    lst = adj_list(vertex, edges)
    g = ig.Graph(edges=lst, directed=True)

    n = len(vertex.keys())

    if color:
        color_dict = ["red", "yellow", "orange", "white"]
        g.vs["color"] = [k for k in color_dict for _ in range(n//4)]

    if nom == 'user':
        g.vs['label'] = get_keys_to_list(vertex)
    else:
        g.vs['label'] = [i for i in range(n)]

    return ig.plot(g)
