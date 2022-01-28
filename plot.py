from cmath import inf
import pandas as pd
import matplotlib.pyplot as plt
from extract_data import *
from datetime import datetime, timedelta
from affichage import most_connected_nodes
path = "data/"
df_accounts = pd.read_csv(path+"instagram_accounts.csv")
df_posts = pd.read_csv(path+"instagram_post_9-11_16-11.csv")


def plot_like_views():
    """affiche le graph du nombre de likes en fonction du nombre de vues
    """
    vues = []
    likes = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        v, l = nb_likes_vue(id_post)
        likes.append(l)
        vues.append(v)
    plt.xlabel('Nombre de vues')
    plt.ylabel('Nombre de likes')
    plt.title("Evolution du nombre de likes en fonction du nombre de vues")
    plt.scatter(vues, likes)
    plt.show()


def follow_fonction_vues():
    vues = []
    follow = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        v, f = nb_vues_follow(id_post)
        follow.append(f)
        vues.append(v)
    plt.scatter(follow, vues)
    plt.show()


def plot_like_follower():
    """plot le graph du nombre de like en fonction du nombre de follower
    """
    nb_follo = []
    likes = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        l, n = number_rapport_likes(id_post)
        likes.append(l)
        nb_follo.append(n)
    plt.xlabel('Nombre de followers')
    plt.ylabel('Nombre de likes')
    plt.title("Evolution du nombre de likes en fonction du nombre de followers")
    plt.scatter(nb_follo, likes)
    plt.show()


def plot_like_date():
    """Affiche les likes en fonctions date
    """
    time = []
    likes = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        post = df_posts.iloc[post]
        date = post['date'] + '-' + post['time']
        date = datetime.strptime(date, '%d/%m/%Y-%H:%M')
        if post['half_day'] == 'pm':
            date += timedelta(hours=12)
        time.append(date)
        likes.append(post['likes'])
    # print(time)
    plt.xlabel('Date du post')
    plt.ylabel('Nombre de likes')
    plt.title("Evolution du nombre de like en fonction de la date du post")
    plt.scatter(time, likes)
    plt.show()


def plot_like_time():
    """Affiche les likes en fonctions du temps
    """
    time = []
    likes = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        post = df_posts.iloc[post]
        date = post['time']
        date = datetime.strptime(date, '%H:%M')
        if post['half_day'] == 'pm':
            date += timedelta(hours=12)
        time.append(date)
        likes.append(post['likes'])
    # print(time)
    plt.xlabel('Heure du post')
    plt.ylabel('Nombre de likes')
    plt.title("Evolution du nombre de likes en fonction de l'heure de post")
    plt.scatter(time, likes)
    plt.show()


def plot_distribution_node_degree(vertex, edges, pas=10):
    """Affiche la distribution des degrées des noeuds dans le graph

    Args:
        vertex ([type]): [description]
        edges ([type]): [description]
        pas (int, optional): [description]. Defaults to 10.
    """
    influenceurs, v = most_connected_nodes(vertex, edges, return_value=True)
    compteur = [0]*v[0]
    for i in v:
        compteur[i-1] += 1
    groupage = [0]*((v[0]//pas))
    if v[0] % pas != 0:
        groupage.append(0)
    for i in range(0, (v[0]//pas)):
        for j in range(i*pas, (i+1)*(pas)):
            groupage[i] += compteur[j]
    plt.xlabel("Degrée des noeuds")
    plt.ylabel("Nombre de noeuds correspondant")
    plt.title("Distribution des degrées des noeuds")
    plt.plot(range(0, v[0], pas), groupage)


def plot_histo_follo():
    """Evolution du nombre de comptes en fonction du nombre de followers
    """
    nb_follo = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        l, n = number_rapport_likes(id_post)
        nb_follo.append(n)
    plt.hist(nb_follo)
    plt.xlabel("Nombre de followers")
    plt.ylabel("Nombre de compte correspondant")
    plt.title('Evolution du nombre de comptes en fonction du nombre de followers')
    plt.show()


def plot_histo_likes():
    likes = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        l, n = number_rapport_likes(id_post)
        likes.append(l)
    plt.xlabel("Nombre de likes")
    plt.ylabel("Nombre de post correspondant")
    plt.hist(likes)


def plot_histo_follow_user():
    likes = []
    for i in range(0, len(df_accounts)):
        user = df_accounts.index[i]
        id_user = df_posts.iloc[user]['id_user']
        l = number_of_like_generated(id_user)
        likes.append(l)
    plt.hist(likes)
    plt.xlabel("Nombre de likes générés")
    plt.ylabel("Nombre de compte correspondant")
    plt.show()
