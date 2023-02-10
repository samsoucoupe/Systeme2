import os

if __name__ == '__main__':
    os.environ["PATH"] = os.environ["PATH"] + ":/tp1"
    os.execvp("python3", ["python3", "afficheur.py"])