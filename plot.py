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
    """affiche le graph du nombre de like en fonction du nombre de views
    """
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
    plt.scatter(time, likes)
    plt.show()


def proba_dessin(vertex, edges, pas=10):
    influenceurs, v = most_connected_nodes(vertex, edges, return_value=True)
    compteur = [0]*v[0]
    for i in v:
        compteur[i-1] += 1
    groupage = [0]*((v[0]//pas))
    if v[0] % pas != 0:
        groupage.append(0)
    for i in range(0, (v[0]//pas)):
        for j in range(i*pas, (i+1)*(pas)):
            print(i, j)
            groupage[i] += compteur[j]
    plt.plot(range(0, v[0], pas), groupage)


def plot_histo_follo():
    nb_follo = []
    for i in range(0, len(df_posts)):
        post = df_posts.index[i]
        id_post = df_posts.iloc[post]['id_post']
        l, n = number_rapport_likes(id_post)
        nb_follo.append(n)
    plt.hist(nb_follo)
    plt.xlabel("Nombre de followers")
    plt.ylabel("Nombre de compte correspondant")
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


def plot_histo_like_follower():
    """plot l'histogram du nombre de like en fonction du nombre de follower
    """
    likes = [0 for i in range(0, 29)]
    influenceurs, valeur = classement_influenceurs_follow(True)
    while influenceurs != []:
        id_user = influenceurs.pop()
        n = number_of_like_generated(id_user)
        print(n)
        f = get_nb_followers(id_user)
        for i in range(0, 29):
            if 10 * i < f <= 10 * i + 10:
                likes[i] += n
    print(likes)
    plt.hist(likes)
    plt.xlabel("Nombre de folowers")
    plt.ylabel("Nombre de likes générés")
    plt.show()
