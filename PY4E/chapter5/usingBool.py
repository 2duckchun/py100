found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 41 :
        found = True
    else :
        found = False
    print(found, value)
print('After', found)