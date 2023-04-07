# Le serveur doit :
# 1. Créer sa propre FIFO (donner un nom unique dans /tmp/, en intégrant le PID du
# serveur dans le nom,
# 2. Programmer une suppression de celle-ci à la terminaison du processus (module
# atexit),
# 3. Ouvrir sa FIFO en lecture,
# 4. Lire les données envoyées par le client (ces données doivent être le chemin de la
# FIFO du client),
# 5. Ouvir la FIFO client en écriture,
# 6. Faire le travail prévu (appel de la fonction server du TD).

import os, sys, atexit

_MAXBYTES = 1000


def server(readfd, writefd):
    while True:
        buff = os.read(readfd, _MAXBYTES)
        if len(buff) == 0:
            break
        os.write(writefd, buff)

def _clean(filename, wfd):
    os.close(wfd)
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    serverfifo = "/tmp/server"+str(os.getpid())
    os.mkfifo(serverfifo)
    print('Fifo created:', serverfifo)
    rfd = os.open(serverfifo, os.O_RDONLY)
    wfd = os.open(os.read(rfd, _MAXBYTES).decode('utf-8'), os.O_WRONLY)
    atexit.register(_clean, serverfifo, wfd)
    server(rfd, wfd)
    sys.exit(0)