#!/usr/bin/env python3
import os
import sys


def main():
    # Verification du nombre de paramètres
    if len(sys.argv) < 2:
        print("Usage: %s cmd [args]" % sys.argv[0])
        sys.exit(1)
    # Récupération de la commande passée en paramètre
    cmd = sys.argv[1:]

    # Exécution de la commande
    os.execv(cmd[0], cmd)

    # sortie du processus fils
    sys.exit(0)


if __name__ == '__main__':
    main()
