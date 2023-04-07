#programme long avec argument

#mytime.py [-n k] [-s] commande [arg ...]



import sys

n=sys.argv[1]

for i in range(int(n)):
    print("hello")
