import igraph as ig
import matplotlib.pyplot as plt
from extract_data import *
from utility import *
from extract_data import *
from affichage import *
from plot import *


def main():
    #vertex, edges = graph()
    """vertex = {14215: 0, 14216: 1, 14235: 2, 14555: 3}
    edges = {14215: [14216, 14555], 14216: [
        14235, 14215], 14235: [14215, 14555]}"""
    #new_vertex, new_edges = degree_min(vertex, edges, 150)
    #afficher_graph(vertex, edges)
    #afficher_graph(new_vertex, new_edges)
    pass


def like_views():
    vues = []
    likes = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        v, l = nb_likes_vue(id_post)
        likes.append(l)
        vues.append(v)
    plt.scatter(vues, likes)
    plt.show()


def like_follow():
    vues = []
    follow = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        v, f = nb_vues_follow(id_post)
        follow.append(f)
        vues.append(v)
    plt.scatter(vues, follow)
    plt.show()


if __name__ == '__main__':
    # main()
    print(moyenne_like())
