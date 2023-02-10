import errno, os, sys


nbChildren = 20
child_pids = []
for i in range(nbChildren):
    pid = os.fork()
    if pid == 0:  # child
        sys.exit(100 + i)
    else:
        child_pids.append(pid)

for pid in child_pids:
    try:  # parent waits for the child to terminate
        pid, status = os.waitpid(pid, 0)
        if os.WIFEXITED(status):
            print(
                "child {} terminated normally with exit status={}".format(
                    pid, os.WEXITSTATUS(status)
                )
            )
        else:
            print("child {} terminated abnormally".format(pid))
    except OSError as e:
        print(
            "waitpid error: {}, {}".format(errno.errorcode[e.errno], os.strerror(e.errno)),
            file=sys.stderr)
        if e.errno == errno.ECHILD:
            print("No more children left. Bye", file=sys.stderr)
sys.exit(0)

