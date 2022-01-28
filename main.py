from extract_data import *
from utility import *
from extract_data import *
from affichage import *
from plot import *
from strategie import *
from propagation import *
from generation import *


def main():
    """vertex, edges = graphe_aléatoire_powerlaw(12, m=25)
    nv, ne = limiter_graph(vertex, edges, 12)
    afficher_graph(nv, ne, nom='user', color=True)"""
    """strategie = random_post(vertex, edges, p=0.01)
    tps, nb_like, nb_personne_like, nb_personne_repost = propagation(
        vertex, edges, strategie, time=40)
    afficher_propagation(tps, nb_like, nb_personne_like,
                         nb_personne_repost)"""
    print(moyenne())


if __name__ == '__main__':
    main()
