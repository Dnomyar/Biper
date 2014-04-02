# -*- coding: utf8 -*-
# AUTEUR   : Damien
# CREATION : 02/04/2014
# VERSION  : 0.2

# Aide technique : http://www.utc.fr/~mecagom4/MECAWEB/EXEMPLE/EX13/WEB/piano.htm

import winsound


# Fréquence du La3 :
fLa3 = 440

# Constante : racine 12ième de 2. Elle permet de conserver un rapport de 2 entre 2 octaves.
a = 1.059463


# ROLE : récupérer la fréquence d'une note
# ARG 1 (note) = la note (par exemple : "do")
# ARG 2 (num) = octave de la note (par exemple : 3)
def getFrequence(note, num):

    numLa3 = 3

    # (nom de la note, distance avec La)
    listNote = [("do", -9),("re", -7),("mi", -5),("fa", -4),("sol", -2),("la", 0),("si", 2)]

    # Si on veut do4 => 12 - 9 = 3

    # On récupère un liste contenant un tuple qui correspond a la note passée en paramètre. Note non trouvée -> []
    res = [item for item in listNote if note in item]

    if res:
        # n : nombre de demi-ton de décalage avec La3
        n = ((num - numLa3) * 12) + res[0][1]
    else:
        print("La note n'est pas dans la liste")

    return (a**n) * fLa3


def play(listNotes):
    for x in listNotes:
        f = int(getFrequence(x[0],x[1]))
        winsound.Beep(f, x[2] * 200)

# notes = [("do", 3),("re", 3),("mi", 3),("fa", 3),("sol", 3),("la", 3),("si", 3)]

# notes2 = [("do", 3),("re", 3),("mi", 3),("fa", 3),("sol", 3),("la", 3),("si", 3),("do", 4),("re", 4),("mi", 4),("fa", 4),("sol", 4),("la", 4),("si", 4),("do", 5),("re", 5),("mi", 5),("fa", 5),("sol", 5),("la", 5),("si", 5),("do", 6)]

# auClairDeLaLune = [("sol", 3),("sol", 3),("sol", 3),("la", 3),("si", 3),("la", 3),("sol", 3),("si", 3),("la", 3),("la", 3),("sol", 3)]

# Une note est définie par son nom (1), son "octave" (2) et sa durée ('1' (Croche), '2' (Noire), '4' (Blanche) ou '6' (Blanche pointée))
# -> (nom, octave, durée)

lettreAElise = [("fa", 4, 1),("mi", 4, 1),("fa", 4, 1),("mi", 4, 1),("fa", 4, 1),("si", 3, 1),("re", 4, 1),("do", 4, 1),("la", 3, 1)]

play(lettreAElise)
