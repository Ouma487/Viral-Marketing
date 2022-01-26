import pandas as pd
import matplotlib.pyplot as plt
from extract_data import number_rapport_likes
from datetime import datetime, timedelta
path = "data/"
df_accounts = pd.read_csv(path+"instagram_accounts.csv")
df_posts = pd.read_csv(path+"instagram_posts_0911_1111.csv")


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
