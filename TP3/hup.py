import os, signal, time

if __name__ == "__main__":
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    pid = os.getpid()
    print("pid", pid)
    n = 0
    while n<3:
        time.sleep(10)
        print("Alive",n)
        n+=1
