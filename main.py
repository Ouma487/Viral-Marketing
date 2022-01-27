from extract_data import *
from utility import *
from extract_data import *
from affichage import *
from plot import *
from strategie import *
from propagation import *


def main():
    vertex, edges = graph()
    #propagation(vertex, edges, random_post(vertex, edges, 0.01), 50)
    #propagation(vertex, edges, best_influenceurs(vertex, edges, 30)[0], 50)

    nv, ne = limiter_graph(vertex, edges, 100)
    afficher_graph(nv, ne, nom='nb', color=True)
    plt.show()


def test():
    print(diff_time_repost(991154137))


if __name__ == '__main__':
    # main()
    test()
