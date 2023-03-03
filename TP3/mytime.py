#mytime.py [-n k] [-s] commande [arg ...]
#Le programme exécute la commande avec ses arguments éventuels, attend sa terminaison affche la durée d'exécution de la commande en secondes et microsecondes.

#Si l'option -n est présente, la même chose est faite k fois (k > 0) ; de plus la durée
#moyenne est affchée.

# Si l'option -s est présente, le programme ache également chaque
#fois le code de sortie de la commande


import os
import sys
import time
import signal

def usage():
    print("Usage mytime.py [-n k] [-s] commande [arg ...]")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:usage()

    nb = 1
    affiche_sortie = False
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-n":
            nb = int(sys.argv[i+1])
            i += 2
        elif sys.argv[i] == "-s":
            affiche_sortie = True
            i += 1
        else:
            break

    if i == len(sys.argv):usage()

    commande = sys.argv[i]
    args = sys.argv[i+1:]

    temps_total = 0
    for i in range(nb):
        debut = time.time()
        pid = os.fork()
        if pid == 0:
            os.execvp(commande, args)
        else:
            os.wait()
            fin = time.time()
            temps_total += fin - debut
            if affiche_sortie:
                print("Sortie", os.WEXITSTATUS(os.wait()[1]))

    print("Temps total", temps_total)
