import os
import sys


def main():
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            sys.exit(0)
        else:
            print(pid)

    input(
        "Press any key to continue..."
    )
    for i in range(3):
        pid,status = os.wait()
        print(pid,status)

if __name__ == "__main__":
    main()