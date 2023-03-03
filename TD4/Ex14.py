
import os
import signal
import sys
import time

def child(pid):
    print("Fils {} : Début de l'exécution".format(pid))
    time.sleep(3)
    print("Fils {} : Fin de l'exécution".format(pid))
    sys.exit(0)

def handler(sig, frame):
    print("Signal reçu : ", sig)
    pid, status = os.wait()
    print("Le fils {} s'est terminé avec le statut {}".format(pid, status))

if __name__ == "main":
    signal.signal(signal.SIGCHLD, handler)
    for i in range(5):
        pid = os.fork()
        if pid == 0:
            child(i)
        else:
            print("Père : création du fils {}".format(pid))
    while True:
        try:
            signal.pause()
        except KeyboardInterrupt:
            sys.exit(0)