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

    vertex, edges = graphe_aléatoire_powerlaw(3046)

    strategie = best_influenceurs(vertex, edges, nb=5)
    tps, nb_like, nb_personne_like, nb_personne_repost = propagation(
        vertex, edges, strategie, time=40)
    afficher_propagation(tps, nb_like, nb_personne_like,
                         nb_personne_repost)


if __name__ == '__main__':
    # main()
    vertex, edges = graph()
    plot_distribution_node_degree(vertex, edges, pas=1)
    plt.show()
