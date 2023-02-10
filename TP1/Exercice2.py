#env | grep "PATH"

import os

"""Depuis python, il est possible d'accèder directement aux variables de l'environnement. Celles-ci sont stockées dans le dictionnaire os.environ. Écrivez un programme qui ache la valeur de chaque variable d'environnement.
Le nombre de variables d'environnements listées par la commande env ou printenv
est-il le même que celui contenu dans os.environ ? Utilisez wc."""



if __name__ == '__main__':
    for i in os.environ:
        print(i, os.environ[i])