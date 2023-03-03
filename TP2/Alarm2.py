import os
import sys
import time


def main():
    # Création du processus fils
    pid = os.fork()

    if pid == 0:
        # Processus fils
        while True:
            # Vérification de l'existence du processus père
            try:
                os.kill(os.getppid(), 0)
            except OSError:
                # Le processus père n'existe plus
                print("Le processus père n'existe plus.")
                break
            time.sleep(1)
    else:
        # Processus père
        while True:
            # Lecture d'un caractère de l'entrée standard
            c = sys.stdin.read(1)
            if not c:
                # Fin de l'entrée standard
                break
            # Écriture du caractère sur la sortie standard
            sys.stdout.write(c)
            sys.stdout.flush()


if __name__ == '__main__':
    main()
