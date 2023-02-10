#!/usr/bin/env python3
import os
import sys


def indice(liste, element):
    try:
        return liste.index(element)
    except ValueError:
        return -1


def main():
    if len(sys.argv) < 2:
        print("Usage: %s cmd1 args ...--then cmd2 args ...[ --else cmd3 args ...] --fi" % sys.argv[0])
        sys.exit(1)
    else:
        cmd1 = sys.argv[1:indice(sys.argv, "--then")]
        cmd2 = sys.argv[indice(sys.argv, "--then") + 1:indice(sys.argv, "--else")]
        cmd3 = sys.argv[indice(sys.argv, "--else") + 1:indice(sys.argv, "--fi")]

        fils = os.fork()
        if fils == 0:
            try:
                os.execv(cmd1[0], cmd1)
            except:
                print("Erreur d'execution")
                sys.exit(1)
        else:
            status = os.wait()
            try:
                if os.WIFEXITED(status):
                    if os.WEXITSTATUS(status) == 0:
                        print("Execution reussie")
                        os.execv(cmd2[0], cmd2)
                    else:
                        print("Execution echouee")
                        os.execv(cmd3[0], cmd3)
                else:
                    print("Erreur de verification")
                    sys.exit(0)
            except:
                print("Erreur de verification")
                sys.exit(1)


if __name__ == '__main__':
    main()
