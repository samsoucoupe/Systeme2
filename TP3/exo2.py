#!/usr/bin/python
import os
import time,signal,sys

def capter_int(signum, frame):
    print("message 1")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, capter_int)
    pid= os.getpid()
    print("pid",pid)
    signal.pause()