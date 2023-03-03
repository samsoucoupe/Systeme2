import signal,sys,time

#programme qui suspend le processus pendant t secondes et met un message 'interuption en cas de ctrl C
def handler(signum,frame):
    print ("interuption")
    sys.exit(0)
if __name__ == '__main__':
    signal.signal(signal.SIGINT,handler)
    t = int(input("t = "))
    time.sleep(t)
    print ("fin du programme")








