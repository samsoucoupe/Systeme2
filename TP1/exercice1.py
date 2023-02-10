import os



def main():
    print("PID : ", os.getpid())
    print("PPID : ", os.getppid())


if __name__ == '__main__':
    main()