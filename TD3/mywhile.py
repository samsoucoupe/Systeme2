#Écrire le programme principal, qui :
#— recherche l’indice des arguments --do et --done,
#— puis affiche l’usage du programme et le termine si la syntaxe n’est pas respectée

#./mywhile.py cmd1 [args ... ] --do cmd2 [args ...] --done
#— sinon, exécute la commande entre les arguments --do et --done, en affichant le temps d’exécution de la commande en secondes et microsecondes.

import os,sys,time,signal

def usage():
    print("Usage mywhile.py cmd1 [args ... ] --do cmd2 [args ...] --done")
    sys.exit(1)

def indice(liste, element):
    try:
        return liste.index(element)
    except ValueError:
        return -1



if __name__ == "__main__":
    indice_do = indice(sys.argv, "--do")
    indice_done = indice(sys.argv, "--done")
    if indice_do == -1 or indice_done == -1 or indice_do > indice_done:
        usage()
    else:
        while True:
            debut = time.time()
            pid = os.fork()
            if pid == 0:
                os.execvp(sys.argv[1], sys.argv[1:indice_do])
            else:
                pid,status=os.wait()
                fin = time.time()
                print("Temps total", fin - debut)
                if os.WIFEXITED(status):
                    if os.WEXITSTATUS(status) == 0:
                        print("Execution reussi")
                        os.execv(sys.argv[indice_do+1], sys.argv[indice_do+1:indice_done])
                    else:
                        print("Execution echouee")
                        sys.exit(1)
                else:
                    print("Erreur de verification")
                    sys.exit(1)


