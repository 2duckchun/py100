fname = input('type a text file: ')
try:
    fhand = open(fname)
except:
    print('wrong text file')
    quit()

for line in fhand:
    if '@uct' in line:
        print(line.strip())