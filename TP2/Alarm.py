#programme qui recopie l'entrée standard sur la sortie standard octect par octet
# toute les 2 sec il incremente un compteur et l'affiche il se temine quand on attein 5 incrementation

import sys
import time
import signal

counter = 0
nombre_de_fois = 5
duration = 2
def handler(sig, ignore):
    global counter
    counter += 1
    print("\ncounter= {}\n".format(counter))
    if counter >= nombre_de_fois:
        print("fin du programme")
        sys.exit(0)

    signal.alarm(duration)
def quitter(sig, ignore):
    sys.exit(0)
if __name__ == "__main__":
    signal.signal(signal.SIGINT, quitter)
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)
    while counter < nombre_de_fois:
        c = sys.stdin.read(1)
        sys.stdout.write(c)



