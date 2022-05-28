handle = open('PY4E\chapter7\mbox-short.txt')

for line in handle :
    if '@uct.ac.za' in line:
        print(line.rstrip())