import os
import sys

if __name__ == "__main__":
    print("Pere")
    print("PID:", os.getpid())
    print("PPID:", os.getppid())
    print("")

    for i in [0, 1, 2]:
        pid = os.fork()
        if pid == 0:
            if i == 0:
                for j in range(2):
                    pid = os.fork()
                    if pid == 0:
                        print("Petit-fils", j + 1)
                        print("PID:", os.getpid())
                        print("PPID:", os.getppid())
                        sys.exit(0)
                sys.exit(0)


            print("Fils", i + 1)
            print("PID:", os.getpid())
            print("PPID:", os.getppid())
            print("")
            sys.exit(0)
        else:
            os.waitpid(pid, 0)
    sys.exit(0)
