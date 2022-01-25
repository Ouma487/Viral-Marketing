import pandas as pd
import numpy as np

path = "data/"

df_accounts = pd.read_csv(path+"instagram_accounts.csv")
df_posts = pd.read_csv(path+"instagram_posts_0911_1111.csv")


def transform_to_list(l):
    """Passe d'une chaine de caractere en une liste donc de:
    '[1, 2, 3]' -> [1, 2, 3]

    Args:
        l (string): chaine de caractere d'une liste

    Returns:
        list: liste
    """
    j = l[0][1:len(l[0])-1]
    o = []
    k = ""
    for i in range(0, len(j)):
        if j[i] == ",":
            o.append(k)
            k = ""
        elif i == len(j) - 1:
            k += j[i]
            o.append(k)
        elif j[i] == " ":
            continue
        else:
            k += j[i]

    res = []
    for elt in o:
        res.append(int(elt))

    return res


def data_frame_post_origin():
    """renvoie un dataframe composé des post orginaux

    Returns:
        dataframe: df_posts ou id_post_origin = 0
    """
    df = df_posts[df_posts['id_post_origin'] == 0]
    return df


def max_repost():
    post_max = np.max(df_posts['reposts'])
    post = df_posts[df_posts.reposts == post_max].index[0]
    ligne = pd.DataFrame(df_posts.loc[post])
    return ligne.loc['reposts'], ligne.loc['id_post']


def number_of_likes(id_post):
    post = df_posts[df_posts['id_post'] == id_post].index[0]
    ligne = pd.DataFrame(df_posts.loc[post])
    return ligne.loc['likes'].astype(str).astype(int)


def number_of_like_generated(id_user):
    """renvoie le nombre de like qu'un utilisateur genere (via ses post et repost)

    Args:
        id_user (int): l'id de l'user considéré
    """
    df_user = df_posts[df_posts['id_user'] == id_user]
    return df_user['likes'].sum()


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


def number_rapport_likes(id_post):
    post = df_posts[df_posts['id_post'] == id_post].index[0]
    id_user = df_posts.iloc[post]['id_user']
    likes = df_posts.iloc[post]['likes']
    user = df_accounts[df_accounts['id_user'] == id_user].index[0]
    nb_followers = df_accounts.iloc[user]['nb_followers']
    return likes, nb_followers
