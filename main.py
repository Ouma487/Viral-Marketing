from extract_data import *
from utility import *
from extract_data import *
from affichage import *
from plot import *
from strategie import *
from propagation import *
from generation import *


def main():
    vertex, edges = graphe_aléatoire_powerlaw(40, m=80)
    #propagation(vertex, edges, random_post(vertex, edges, 0.01), 50)
    #propagation(vertex, edges, best_influenceurs(vertex, edges, 30)[0], 50)
    #afficher_graph(vertex, edges)
    nv, ne = limiter_graph(vertex, edges, 20)
    afficher_graph(nv, ne, nom='nb', color=True)
    plt.show()


def test():
    plot_histo_like_follower()


if __name__ == '__main__':
    main()
    # test()
    pass
