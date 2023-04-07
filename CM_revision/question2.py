import sys,os,signal
import time


def handler_c(sig,signum):
    if os.fork() ==0:
        time.sleep(2)
        sys.exit()




if __name__ == "__main__":
    signal.signal(signal.SIGUSR1,handler_c)
    while True:
        pid,status = os.wait()
        print(f"le fils pid={pid} est terminé")
