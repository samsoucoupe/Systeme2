#!/usr/bin/env python3
import os
import sys


def verifier(com, args):


    fils = os.fork()
    if fils==0:
        try:
            os.execv(com, args)
        except:
            print("Erreur d'execution")
            sys.exit(1)
    else:
        status = os.wait()
        try:
            if os.WIFEXITED(status):
                if os.WEXITSTATUS(status) == 0:
                    print("Execution reussie")
                else:
                    print("Execution echouee")
            else:
                print("Erreur de verification")
            sys.exit(0)
        except:
            print("Erreur de verification")
            sys.exit(1)







if __name__ == "main":
    if len(sys.argv) < 2:
        print("Usage : ./verifier.py com arg1 .. argn")
        sys.exit(1)
    else:
        com = sys.argv[1]
        args = sys.argv[1:]
        verifier(com, args)
