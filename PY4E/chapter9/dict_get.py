counts = dict()
names = ['김', '박', '최', '윤', '박']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)