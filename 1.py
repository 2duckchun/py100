x = input('입력 : ') # xyz321 입력
a = [ 'abc123', 'def456', 'ghi789']
a.append(x)
a.remove('def456') # 'abc123', 'ghi789'. 'xyz321'
print(a[1][-3:], a[2][:-3], sep = ",") # 789,xyz
for i in range(3, 6):
    print(i, end=" ") # 3 4 5