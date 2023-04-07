import atexit, os, select, signal, sys

_MAXBYTES = 1000

_SEPARATOR = '$'


def INT_handler(s, _):
    os.write(wfd, (myfifo + _SEPARATOR).encode('utf-8'))  # envoyer message de deconnexion vers serveur
    sys.exit(130)


def client(readfd, writefd, myfifo):
    while True:
        rds,_,_=select.select([readfd,0], [], [])
        for fd in rds:
            buff = os.read(fd, _MAXBYTES)
            if fd == readfd:
                os.write(1, buff)
            elif fd == 0:
                os.write(writefd, (myfifo + _SEPARATOR).encode('utf-8') + buff)  # envoyer contenu sur tube vers serveur
                if len(buff) == 0:
                    return
            else:
                print("erreur", file=sys.stderr)
                print(buff)
                print(fd,readfd)







def _clean(filename, wfd):
    print("clean-up", file=sys.stderr)
    os.close(wfd)
    try:
        os.unlink(filename)
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    signal.signal(signal.SIGINT, INT_handler)
    if len(sys.argv) < 2:
        print("usage: %s <server's fifo name>" "/tmp/client" + str(os.getpid()))
        sys.exit(1)
    myfifo = "/tmp/client" + str(os.getpid())
    os.mkfifo(myfifo)
    print('Fifo created:', myfifo)
    serverfifo="/tmp/"+sys.argv[1]
    wfd = os.open(serverfifo, os.O_WRONLY)
    atexit.register(_clean, myfifo, wfd)
    os.write(wfd, (_SEPARATOR + myfifo).encode('utf-8'))  # write fifo name to server
    rfd = os.open(myfifo, os.O_RDONLY)
    client(rfd, wfd, myfifo)
    sys.exit(0)
