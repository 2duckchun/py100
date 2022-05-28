han = open('PY4E\chapter7\mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    print('words:', wds)
    if wds[0] != 'From' :
        print('ignore')
        continue
    print(wds[2])