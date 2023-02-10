import os
import time


#1

pid = os.getpid()
# Le processus père affiche son PID
print("PID du père:", pid)
# Le processus père crée un fils
pid = os.fork()
# Le fils affiche son PID et s'endort 5 secondes
if pid == 0:
    print("PID du fils:", os.getpid())
    time.sleep(5)
    exit()
# Le père affiche un message signalant que son fils est mort
else:
    os.wait()
    print("Le fils est mort.")



#2
print(" Parti 2")

print("PID du processus père :", os.getpid())
pid = os.fork()
if pid == 0:
    # code exécuté par le fils
    print("PID du processus fils :", os.getpid())
else:
    # code exécuté par le père
    os.waitpid(pid, 0)
    print("Code de sortie du fils :", os.WEXITSTATUS(pid))
