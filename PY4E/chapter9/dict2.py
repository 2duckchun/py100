counts = dict()
names = ['김', '박', '최', '윤', '박']
for name in names :
    if name in counts :
        counts[name] = counts[name] + 1
    else :
        counts[name] = 1
print(counts)

counts2 = dict()
names2 = ['김', '박', '최', '윤', '박']
for name2 in names2 :
    if name2 not in counts2 :
        counts2[name2] = 1
    else :
        counts2[name2] = counts2[name2] + 1
print(counts2)