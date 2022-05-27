handle = open('PY4E\chapter7\mbox-short.txt')

for line in handle :
    if not '@uct.ac.za' in line:
        continue
    print(line.rstrip())