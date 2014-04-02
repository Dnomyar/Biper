# -*- coding: utf8 -*-
# AUTEUR   : Damien
# CREATION : 02/04/2014
# VERSION  : 0.2

# Aide technique : http://www.utc.fr/~mecagom4/MECAWEB/EXEMPLE/EX13/WEB/piano.htm

import winsound
from songs import *

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
    listNote = [("do", -9),("do#", -8),("reb", -8),("re", -7),("re#", -6),("mib", -6),("mi", -5),("fa", -4),("fa#", -3),("solb", -3),("sol", -2),("sol#", -1),("lab", -1),("la", 0),("la#", 1),("sib", 1),("si", 2)]

    # Si on veut do4 => 12 - 9 = 3

    # On récupère un liste contenant un tuple qui correspond a la note passée en paramètre. Note non trouvée -> []
    res = [item for item in listNote if note in item]

    n = 0
    if res:
        # n : nombre de demi-ton de décalage avec La3
        n = ((num - numLa3) * 12) + res[0][1]
    else:
        print("La note n'est pas dans la liste")

    return (a**n) * fLa3


def player(song):
    for x in song[1]:
        f = int(getFrequence(x[0],x[1]))
        tempo = int(song[0] * x[2])
        winsound.Beep(f, tempo)



player(lettreAElise())
