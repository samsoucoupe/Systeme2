# import os, sys
# fd1 = os.open("toto.txt", os.O_RDONLY)
# bytes_sequence = os.read(fd1, 2) # séquence d'octets
# print(bytes_sequence)
# print(bytes_sequence.decode("utf-8"))
# bytes_sequence = os.read(fd1, 1)
# os.close(fd1)
# print(bytes_sequence)
# print(bytes_sequence.decode("utf-8"))
# sys.exit(0)


# import os, sys
# fd1 = os.open("toto.txt", os.O_RDONLY)
# fd2 = os.open("toto.txt", os.O_RDONLY)
#
# bytes_sequence = os.read(fd1, 2) # séquence d'octets
# bytes_sequence = os.read(fd2, 6)
# os.close(fd1)
# os.close(fd2)
# print(bytes_sequence)
# print(bytes_sequence.decode("utf-8"))
# print(bytes_sequence.decode("latin-1"))
# sys.exit(0)


# import os, sys
# fd = os.open("toto.txt", os.O_RDONLY)
# pid = os.fork()
# if pid == 0:
#     c = os.read(fd, 1)
#     sys.exit(0)
# os.wait()
# c = os.read(fd, 1)
# print(c)
# sys.exit(0)

import os, sys
fd1 = os.open("titi.txt", os.O_RDONLY)
fd2 = os.open("titi.txt", os.O_RDONLY)
c = os.read(fd2, 1)
os.dup2(fd2, fd1)
c = os.read(fd1, 1)
os.close(fd1)
os.close(fd2)
print(c)
sys.exit(0)
