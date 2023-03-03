# , implémenter un programme qui :  lors de la fermeture du programme, ache un message de sortie par l'intermédiaire du module atexit. Ce programme doit proposer deux terminaisons diérentes

import atexit
import os
import signal
import sys
import time

signal_exit = ""


def capter_int(signum, frame):
    global signal_exit
    print("message signal sigint")
    signal_exit = "SIGINT"


def capter_term(signum, frame):
    global signal_exit
    print("message signal sigterm")
    signal_exit = "SIGTERM"


def capter_quit(signum, frame):
    global signal_exit
    print("message signal sigquit")
    signal_exit = "SIGQUIT"


def capter_abrt(signum, frame):
    global signal_exit
    print("message signal sigabrt")
    signal_exit = "SIGABRT"


def fin():
    print("Au revoir\n je suis mort par in signal : ", signal_exit)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, capter_int)
    signal.signal(signal.SIGTERM, capter_term)
    signal.signal(signal.SIGQUIT, capter_quit)
    signal.signal(signal.SIGABRT, capter_abrt)

    atexit.register(fin)
    while signal_exit == "":
        time.sleep(1)
        print("Alive")
