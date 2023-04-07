# Le client doit :
# 1. Créer sa propre FIFO (donner un nom unique dans /tmp/, en intégrant le PID du
# serveur dans le nom,
# 2. Programmer une suppression de celle-ci à la terminaison du processus (module
# atexit),
# 3. Récupérer le chemin de la FIFO serveur comme 1er argument de la ligne de com-
# mande et l'ouvrir en écriture,
# 4. Envoyer le chemin de sa propre FIFO au serveur,
# 1
# 5. Ouvrir sa propre FIFO en lecture,
# 6. Faire le travail prévu (appel de la fonction client du TD).


import atexit, os, sys

_MAXBYTES = 1000


def client(readfd, writefd):
    while True:
        inputbuff = os.read(0, _MAXBYTES)
        if len(inputbuff) == 0:
            break
        os.write(writefd, inputbuff)
        buff = os.read(readfd, _MAXBYTES)
        if len(buff) == 0:
            break
        os.write(1, buff)


def _clean(filename, wfd):
    print("clean-up", file=sys.stderr)
    os.close(wfd)
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: %s <server's fifo name>" % str(os.getpid()))
        sys.exit(1)
    myfifo = "/tmp/client" + str(os.getpid())
    os.mkfifo(myfifo)
    serverfifo = "/tmp/"+ sys.argv[1]
    wfd = os.open(serverfifo, os.O_WRONLY)
    atexit.register(_clean, myfifo, wfd)
    os.write(wfd, myfifo.encode('utf-8'))
    rfd = os.open(myfifo, os.O_RDONLY)
    client(rfd, wfd)
    sys.exit(0)
