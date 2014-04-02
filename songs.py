# -*- coding: utf8 -*-
# AUTEUR   : Damien
# CREATION : 02/04/2014

from typesDeNote import *

# Les fonctions doivent retourner un liste contenant 2 éléments :
#   - le premier : le "tempo" (plus est grand plus c'est rapide)
#   - le second : la liste des notes
#       une note es une tulpe composée de 3 éléments :
#           - nom de la note
#           - son "octave"
#           - et sa durée (relative au tempo)




# =========================
# Lettre à Elise de Paul D.
# =========================
def lettreAElise():

    # On charge la musique
    t = TypeDeNotes()

    m1 = [("mi", 5, t.DC), ("re#", 5, t.DC)]
    m2 = [("mi", 5, t.DC), ("re#", 5, t.DC),("mi", 5, t.DC), ("si", 4, t.DC), ("re", 5, t.DC), ("do", 5, t.DC)]
    m3 = [("la", 4, t.CP), ("do", 4, t.DC), ("mi", 4, t.DC), ("la", 4, t.DC)]
    m4 = [("si", 4, t.CP), ("mi", 4, t.DC), ("sol#", 4, t.DC), ("si", 4, t.DC)]
    m5 = [("do", 5, t.CP), ("mi", 4, t.DC), ("mi", 5, t.DC), ("re#", 5, t.DC)]
    m6 = [("mi", 5, t.DC), ("re#", 5, t.DC),("mi", 5, t.DC), ("si", 4, t.DC), ("re", 5, t.DC), ("do", 5, t.DC)]
    m7 = [("la", 4, t.CP), ("do", 4, t.DC), ("mi", 4, t.DC), ("la", 4, t.DC)]
    m8 = [("si", 4, t.CP), ("mi", 4, t.DC), ("do", 5, t.DC), ("si", 4, t.DC)]
    m9 = [("la", 4, t.CP), ("si", 4, t.DC), ("do", 5, t.DC), ("re", 5, t.DC)]
    m10 = [("mi", 5, t.CP), ("sol", 4, t.DC), ("fa", 5, t.DC), ("mi", 5, t.DC)]
    m11 = [("re", 5, t.CP), ("fa", 4, t.DC), ("mi", 5, t.DC), ("re", 5, t.DC)]
    m12 = [("do", 5, t.CP), ("mi", 4, t.DC), ("re", 5, t.DC), ("do", 5, t.DC)]
    m13 = [("si", 4, t.DC), ("mi", 3, t.DC), ("mi", 4, t.DC), ("mi", 4, t.DC), ("mi", 5, t.DC), ("mi", 4, t.DC)]
    m14 = [("mi", 5, t.DC), ("mi", 5, t.DC), ("mi", 6, t.DC), ("re#", 5, t.DC), ("mi", 5, t.DC), ("re#", 5, t.DC)]
    m15 = [("mi", 5, t.DC), ("re#", 5, t.DC),("mi", 5, t.DC), ("re#", 5, t.DC), ("mi", 5, t.DC), ("re#", 5, t.DC)]

    # reprise mesures 2,3,4,5,6,7,8,9
        #reprise mesure 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9

    bpm = 250

    return [bpm, m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12 + m13 + m14 + m15 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9 + m10 + m11 + m12 + m13 + m14 + m15 + m2 + m3 + m4 + m5 + m6 + m7 + m8]


