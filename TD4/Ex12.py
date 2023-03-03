import signal,sys,time
#programme qui boucle dans le vide et envoi un signalAlarme toutes les seconde  et affiche bip a chaque fois et au 6eme affiche bye et termine le programme
def handler(signum,frame):
    print ("bip")
    global i
    i+=1
    if i==5:
        print ("bye")
        sys.exit(0)
    signal.alarm(1)
if __name__ == '__main__':
    signal.signal(signal.SIGALRM,handler)
    i=0
    signal.alarm(1)
    while True:
        signal.pause()