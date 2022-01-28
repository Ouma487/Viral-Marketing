from utility import get_keys_to_list, adj_list, var
import igraph as ig
import matplotlib.pyplot as plt


def most_connected_nodes(vertex, edges, return_value=False):
    """Return nom/id des noeuds les plus connectés

    Args:
        vertex ([type]): [description]
        edges ([type]): [description]
    Return:
        liste: liste des influenceurs par ordre décroissant de de followers
        (si return_value = True) liste: nombre de followers des influenceurs
    """
    influenceurs = []
    valeur = []
    for id_node in edges.keys():
        followers = len(edges[id_node])
        n = len(valeur)
        i = 0
        while i < n and followers < valeur[i]:
            i += 1
        valeur.insert(i, followers)
        influenceurs.insert(i, id_node)
    if not return_value:
        return influenceurs
    else:
        return influenceurs, valeur


def limiter_graph(vertex, edges, N):
    """Permet de réduire le graph à afficher en conservant que les noeuds les plus connectées.
    Et les liaisons entre ses noeuds les plus connectées.
    Remarque :
    new_vertex est un dictionnaire ou les clefs sont dans l'ordre des noeuds les plus connectés
    de vertex.
    Args:
        vertex (dic)
        edges (dic)
        N (int): nombre de noeuds à conserver

    Returns:
        new_vertex, new_edges
    """
    id_infuenceurs = most_connected_nodes(vertex, edges)[:N]
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
    """Affiche 3 graphs qui décrivent la propagation de l'information dans le graph

    Args:
        tps (list)
        nb_like (list)
        nb_personne_like (list)
        nb_personne_repost (list)
    """
    # Dérivée
    fig, axs = plt.subplots(3, 2)
    axs[0, 1].plot(tps, var(nb_like), 'tab:orange')
    axs[0, 1].set_title('Nombre de nouveaux likes à chaque instant')

    axs[1, 1].plot(tps, var(nb_personne_like), 'tab:orange')
    axs[1, 1].set_title(
        "Nombre de nouvelles personnes qui 'like' à chaque instant")

    axs[2, 1].plot(tps, var(nb_personne_repost), 'tab:orange')
    axs[2, 1].set_title(
        "Nombre de nouvelles personnes qui 'repost' à chaque instant")
    # Graph normaux
    axs[0, 0].plot(tps, nb_like, 'tab:green')
    axs[0, 0].set_title('Nombre de likes en fonction du temps')

    axs[1, 0].plot(tps, nb_personne_like, 'tab:green')
    axs[1, 0].set_title("Nombre de personnes qui 'like'")

    axs[2, 0].plot(tps, nb_personne_repost, 'tab:green')
    axs[2, 0].set_title("Nombre de personnes qui 'repost'")
    fig.tight_layout()
    plt.show()


def afficher_graph(vertex, edges, nom='False', color=False):
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
        color_dict = ["red", "orange", "yellow", "white"]
        g.vs["color"] = [k for k in color_dict for _ in range(n//4)]

    if nom == 'user':
        g.vs['label'] = get_keys_to_list(vertex)
    elif nom == 'nb':
        g.vs['label'] = [i for i in range(n)]

    return ig.plot(g)
