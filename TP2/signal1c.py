import os
import signal
import sys


def CHLD_handler(signal, ignore):
    """Traitant de l'interruption SIGCHLD"""
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
        except OSError:
            return

        if pid == 0:
            return

        if os.WIFEXITED(status):
            print("**père** child %d terminated normally with exit status=%d" % (pid, os.WEXITSTATUS(status)))
        else:
            print("**père** child %d terminated abnormally" % pid)


# Programme principal
if __name__ == '__main__':
    signal.signal(signal.SIGCHLD, CHLD_handler)  # Installe le traitant
    for i in range(10):  # Création des fils
        pid = os.fork()
        if pid == 0:
            print("------> fils (pid = %d). Je me termine." % os.getpid())
            sys.exit(1 + i)
        else:
            print("**père** fils créé, pid = %d" % pid)

    # À tout moment l'exécution peut être interrompue par la réception
    # d'un signal SIGCHLD. Si le programme est en train de faire un appel
    # système (par exemple pour attendre une lecture clavier), cette
    # interruption provoque la levée d'une exception.
    # Problème: si on est interrompu pendant qu'on attend une saisie
    # clavier, cette saisie est interrompue.
    # => Il faut donc recommencer la saisie en cas d'exception.
    # Astuce: Pour savoir si la saisie a été interrompue, et donc savoir
    # s'il faut recommencer (avec une boucle while) il suffit de regarder
    # si la variable de saisie existe.
    while not 'saisie' in globals():
        try:
            saisie = input("**père** tapez quelque chose... ")
        except:  # La réception d'un signal provoque l'interruption de la saisie
            pass

    print("**père** Terminé !")
    sys.exit(0)



