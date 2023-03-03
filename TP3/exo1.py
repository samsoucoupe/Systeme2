#!/usr/bin/python3
import time,signal,sys

def capter_int(signum, frame):
    global nb_sig
    nb_sig += 1
    if nb_sig == 2:
        print("Au revoir")
        nb_sig = 0 # pour annuler le 1.3
    else:
        print("OUCH")
        signal.alarm(5)
def capte_alarm(signum, frame):
    global nb_sig
    nb_sig += 10


if __name__ == "__main__":
    nb_sig = 0
    signal.signal(signal.SIGINT, capter_int)
    signal.signal(signal.SIGALRM, capte_alarm)
    signal.alarm(10)
    while nb_sig < 2:
        time.sleep(1)
        print("Alive")