import pandas as pd
import numpy as np
from utility import *
from datetime import datetime, timedelta

path = "data/"

df_accounts = pd.read_csv(path+"instagram_accounts.csv")
df_posts = pd.read_csv(path+"instagram_post_9-11_16-11.csv")


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


def data_frame_post_origin():
    """renvoie un dataframe composé des post orginaux

    Returns:
        dataframe: df_posts ou id_post_origin = 0
    """
    df = df_posts[df_posts['id_post_origin'] == 0]
    return df


def max_repost():
    """Renvoie l'id du post qui a été le plus repost et son nombre de repost
    INCERTAINE
    Returns:
        tuple: [description]
    """
    post_max = np.max(df_posts['reposts'])
    post = df_posts[df_posts.reposts == post_max].index[0]
    ligne = pd.DataFrame(df_posts.loc[post])
    return ligne.loc['reposts'], ligne.loc['id_post']


def number_of_like_generated(id_user):
    """renvoie le nombre de like qu'un utilisateur genere (via ses post et repost)

    Args:
        id_user (int): l'id de l'user considéré
    """
    df_user = df_posts[df_posts['id_user'] == id_user]
    return df_user['likes'].sum()


def classement_influenceurs():
    """Renvoie les ids des influenceurs classés par ordre de ceux qui ont généré le plus de like.
    influenceurs[1] a généré plus de like que inflenceurs[2].

    Returns:
        list: liste des id des influenceurs.
    """
    valeur = []
    influenceurs = []
    for user_id in df_accounts['id_user'].values:
        like = number_of_like_generated(user_id)
        n = len(valeur)
        i = 0
        while i < n and like < valeur[i]:
            i += 1
        valeur.insert(i, like)
        influenceurs.insert(i, user_id)
    return influenceurs


def moyenne_like():
    """renvoie la moyenne des likes

    Returns:
        float: la moyenne des likes du dataframe
    """
    n = len(df_posts)
    return df_posts['likes'].sum() / n


"""def number_rapport_likes(id_post):
    post = df_posts[df_posts['id_post'] == id_post].index[0]
    ligne = pd.DataFrame(df_posts.loc[post])
    id_user = ligne.loc['id_user'].astype(str).astype(int)
    likes = ligne.loc['likes'].astype(str).astype(int)
    return id_user, likes"""


def get_nb_followers(id_user):
    """Renvoie le nombre de follower d'un user

    Args:
        id_user (int): user id
    Return:
        int: nb de follower
    """
    user_index = df_accounts[df_accounts['id_user'] == id_user].index[0]
    return df_accounts.iloc[user_index]['nb_followers']


def number_rapport_likes(id_post):
    post = df_posts[df_posts['id_post'] == id_post].index[0]
    id_user = df_posts.iloc[post]['id_user']
    likes = df_posts.iloc[post]['likes']
    user = df_accounts[df_accounts['id_user'] == id_user].index[0]
    nb_followers = df_accounts.iloc[user]['nb_followers']
    return likes, nb_followers


def nb_likes_vue(id_post):
    post = df_posts[df_posts['id_post'] == id_post].index[0]
    views = df_posts.iloc[post]['views']
    likes = df_posts.iloc[post]['likes']
    return views, likes


def nb_vues_follow(id_post):
    post = df_posts[df_posts['id_post'] == id_post].index[0]
    id_user = df_posts.iloc[post]['id_user']
    views = df_posts.iloc[post]['views']
    user = df_accounts[df_accounts['id_user'] == id_user].index[0]
    nb_followers = df_accounts.iloc[user]['nb_followers']
    return views, nb_followers


def classement_influenceurs_follow():
    """Renvoie les ids des influenceurs classés par ordre de ceux qui ont le plus de followers.
    influenceurs[1] a plus de followers que inflenceurs[2].

    Returns:
        list: liste des id des influenceurs.
    """
    valeur = []
    influenceurs = []
    for user_id in df_accounts['id_user'].values:
        user = df_accounts[df_accounts['id_user'] == user_id].index[0]
        followers = df_accounts.iloc[user]['nb_followers']
        n = len(valeur)
        i = 0
        while i < n and followers < valeur[i]:
            i += 1
        valeur.insert(i, followers)
        influenceurs.insert(i, user_id)
    return influenceurs
