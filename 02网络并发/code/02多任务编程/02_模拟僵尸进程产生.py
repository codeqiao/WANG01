import os
import sys

pid = os.fork()

if pid<0:
    print("Error")

elif pid == 0:
    print("1111111")
    sys.exit("子进程退出")
else:
    while True:
        pass
