import os, signal, sys, time


def handler(signum, frame):
    global nb_sig
    if pid  == 0:
        print("[Fils] Signal reçu")
        if nb_sig < n:
            os.kill(os.getppid(), signal.SIGUSR1)
            nb_sig += 1
    else:
        print("[Père] Signal reçu")
        os.kill(pid, signal.SIGUSR1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: exo1.py n")
        sys.exit(1)
    n = int(sys.argv[1])
    nb_sig = 0
    signal.signal(signal.SIGUSR1, handler)
    pid = os.fork()
    if pid == 0:
        os.kill(os.getppid(), signal.SIGUSR1)
        for i in range(n):
            time.sleep(0.001)
            signal.pause()
        print("[Fils] Fin fils avec ", nb_sig, " signaux reçus")
        sys.exit(0)
    else:
        os.waitpid(pid, 0)
        print("[Père] Fin père avec ", nb_sig, " signaux reçus")
        sys.exit(0)