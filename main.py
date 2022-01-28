import datetime
from matplotlib.style import use
from pip import main
import igraph as ig
import matplotlib.pyplot as plt
from extract_data import *
from utility import *
from extract_data import *
from affichage import *
from plot import *
from strategie import *
from propagation import *
from generation import *


def main():

    vertex, edges = graph()

    strategie = random_post(vertex, edges, p=0.001)
    tps, nb_like, nb_personne_like, nb_personne_repost = propagation(
        vertex, edges, strategie, time=60)
    afficher_propagation(tps, nb_like, nb_personne_like,
                         nb_personne_repost)


if __name__ == '__main__':
    # main()
    v, e = graphe_aléatoire_powerlaw(12, m=30)
    v, e = limiter_graph(v, e, 12)
    afficher_graph(v, e, nom='user', color=True)
