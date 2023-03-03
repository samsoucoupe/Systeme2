import os,sys,signal
import time


def handler(signum, frame):
    global nb_sig
    nb_sig += 1




if __name__ == "__main__":
    nb_sig = 0
    if len(sys.argv) != 2:
        print("usage: exo1.py n")
        sys.exit(1)
    n = int(sys.argv[1])
    signal.signal(signal.SIGUSR1, handler)
    pid = os.fork()
    if pid == 0:
        for i in range(n):
            os.kill(os.getppid(), signal.SIGUSR1)
            time.sleep(0.1)
        sys.exit(0)
    else:
        # modifier le pere pour qu'ilaffiche un message lorque le siguser1 est capturé
        os.waitpid(pid, 0)
        print("fin pere avec ", nb_sig, " signaux reçus")
        sys.exit(0)

