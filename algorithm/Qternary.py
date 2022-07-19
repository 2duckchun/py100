x = int(input('x값 입력: '))
y = int(input('y값 입력: '))
a = x if x > y else y

print(a)

if a == x :
    print('x가 큽니다')
elif a == y :
    print('y가 큽니다')
else :
    print('같거나 문제가 있습니다')