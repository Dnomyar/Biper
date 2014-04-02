# -*- coding: utf8 -*-
# AUTEUR   : Damien
# CREATION : 02/04/2014


class TypeDeNotes:

    # Binaire TEMPS même si la musique est en ternaire à la base
    BASE = 4

    # Noire
    N = BASE

    # Noire pointée
    NP = BASE + BASE/2

    # Croche
    C = N/2

    # Croche pointée
    CP = C + C/2

    # Double croche
    DC = C/2

    # Double croche pointée
    DCP = DC + DC/2

    # Blanche
    B = BASE*2

    # Blanche pointée
    BP = B + BASE

    # Ronde
    R = B*2

    def __init__(self):
        pass
