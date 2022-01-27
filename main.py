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
    #propagation(vertex, edges, random_post(vertex, edges, 0.01), 50)
    #propagation(vertex, edges, best_influenceurs(vertex, edges, 30)[0], 50)
    #afficher_graph(vertex, edges, color=True)
    nv, ne = limiter_graph(vertex, edges, 200)
    afficher_graph(nv, ne, nom='user', color=True)
    proba_dessin(vertex, edges, pas=1)
    print('nb_follow', nb_follow(vertex, edges))
    plt.show()


if __name__ == '__main__':
    main()
    pass
