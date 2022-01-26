from extract_data import *
from utility import *
from extract_data import *
from affichage import *
from plot import *
from strategie import *
from propagation import *


def main():
    vertex, edges = graph()
    #propagation(vertex, edges, random_post(vertex, edges, 0.01), 20)
    propagation(vertex, edges, best_influenceurs(vertex, edges, 20)[0], 20)


def test():
    (proba_dessin())


if __name__ == '__main__':
    # main()
    test()
