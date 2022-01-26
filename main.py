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
    propagation(vertex, edges, best_influenceurs(vertex, edges, 10)[0], 20)


if __name__ == '__main__':
    main()
