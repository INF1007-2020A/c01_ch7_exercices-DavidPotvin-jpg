#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def valide(seq):
    for char in seq:
        if char not in "atcg":
            False
    return True

def saisie():
    return input('chaine :')

def proportion(seq, subseq):
    return 100 * seq.find(subseq)/len(seq)
    

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
