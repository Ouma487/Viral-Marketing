from matplotlib.style import use
from pip import main
import igraph as ig
import matplotlib.pyplot as plt
from extract_data import *
from utility import *

path = "data/"


def graph():
    """Génère vertex et edges

    Returns:
        vertex [dictionnaire]: clés: users_id | valeurs: int: le numéro du noeud (pour des eventuels affichages)
        edges [dictionnaire]: clés: users_id | valeurs: list: les follows_id 
    """
    df = pd.read_csv(path+"instagram_accounts.csv")
    vertex = {}
    edges = {}
    users_id = df[['id_user']].to_numpy()
    followers_id = df[['id_followers']].to_numpy()
    n = len(users_id)
    for i in range(n):
        user_id = users_id[i, 0]
        vertex[user_id] = i
        followers_id_i = transform_to_list(followers_id[i])
        edges[user_id] = followers_id_i
    return vertex, edges


def afficher_graph(vertex, edges):
    """Affiche le graph

    Args:
        vertex (dic): dictionnaire qui a un user_id lui associe son numéro dans le graph
        edges (dic): dictionnaire qui a un user_id lui associe la liste de ses follows_id
    """
    lst = adj_list(vertex, edges)
    g = ig.Graph(edges=lst, directed=True)
    print("en cours")
    g.vs['label'] = get_keys_to_list(vertex)
    ig.plot(g)
    plt.show()


def main():
    vertex, edges = graph()
    """vertex = {14215: 0, 14216: 1, 14235: 2, 14555: 3}
    edges = {14215: [14216, 14555], 14216: [
        14235, 14215], 14235: [14215, 14555]}"""
    #new_vertex, new_edges = degree_min(vertex, edges, 150)
    afficher_graph(vertex, edges)
    #afficher_graph(new_vertex, new_edges)


def traitement_data():
    nb_follo = []
    likes = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        l, n = number_rapport_likes(id_post)
        likes.append(l)
        nb_follo.append(n)
    plt.scatter(nb_follo, likes)
    plt.show()
    print(max(nb_follo))


if __name__ == '__main__':
    # main()
    traitement_data()
