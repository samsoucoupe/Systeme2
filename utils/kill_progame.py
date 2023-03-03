#programme qui kill le processus en argument grace a son nom

#exemple : python3 kill_progame.py Alarm.py

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage : {} nom_du_programme".format(sys.argv[0]))
        sys.exit(1)
    nom = sys.argv[1]
    pid_str = os.popen("pgrep -f {}".format(nom)).read().strip()  # strip pour enlever les espaces en début et fin
    if pid_str == "":
        print("le programme {} n'est pas lancé".format(nom))
        sys.exit(1)
    pid_list = pid_str.split("\n")
    for pid in pid_list:
        pid = int(pid)
        os.execvp("kill", ["kill", "-s","KILL", str(pid)])  # kill -s KILL pid
        print("le programme {} a été tué".format(nom))
    sys.exit(0)
