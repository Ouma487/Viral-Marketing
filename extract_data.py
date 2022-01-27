import pandas as pd
import numpy as np
from utility import *

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


def classement_influenceurs_like(return_value=False):
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
    if not return_value:
        return influenceurs
    else:
        return influenceurs, valeur


def classement_influenceurs_follow(return_value=False):
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
    if not return_value:
        return influenceurs
    else:
        return influenceurs, valeur


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


def taux_repost(id_post):
    post = df_posts[df_posts['id_post'] == id_post].index[0]
    views = df_posts.iloc[post]['views']
    repost = df_posts.iloc[post]['reposts']
    if views == 0:
        return 0
    return repost/views


def moyenne_taux_repost():
    l = []
    for id_post in df_posts['id_post'].values:
        if taux_repost(id_post) < 1:
            l.append(taux_repost(id_post))
    return sum(l)/len(l)


def nb_follow():
    vertex, edges = graph()
    nb_follow = [0]*len(vertex)
    for i in vertex.keys():
        for j in edges[i]:
            nb_follow[vertex[j]-1] += 1
    return nb_follow


def was_repost(id_post):
    post = df_posts[df_posts['id_post_origin'] == id_post]
    return len(post) > 0


def list_time_repost(id_post):
    if not was_repost(id_post):
        return []
    else:
        l = []
        post_1 = df_posts[df_posts['id_post_origin'] == id_post]
        for i in range(0, len(post_1)):
            post = post_1.iloc[i, :]
            l.append((post['date'], post['time'], post['half_day']))
        return(l)


def difference_date(d1, d2):
    a1, b1, c1 = d1
    a2, b2, c2 = d2
    return a2  # exprimer la différence de temps en heure


def diff_time_repost(id_post):
    l = list_time_repost(id_post)
    res = []
    post = df_posts[df_posts['id_post'] == id_post]
    date_ini = ((post['date'], post['time'], post['half_day']))
    for elt in l:
        delta = difference_date(elt, date_ini)
        res.append(delta)
    return res  # liste des ecrats en heure


def diff_repost():
    # dico ou clé int ou les valeurs = nb de delta dans 10 * cle et 10*cle + 10 (en heure)
    dico = {}
    for id_post in df_posts['id_post'].values:
        res = diff_time_repost(id_post)
        for elt in res:
            j = elt//10
            if j in dico:
                dico[j] += 1
            else:
                dico[j] = 1
    return dico
