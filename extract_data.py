
import pandas as pd


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
