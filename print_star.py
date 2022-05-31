# *를 n개 출력하되 w개마다 줄바꿈하기

print('*을 출력합니다.')
n = int(input('*을 몇 개 출력할까요?: '))
w = int(input('몇 개마다 개행할까요?: '))

for _ in range(n // w):
    print('*' * w)
    
if n % w:
    print('*' * (n % w))