# 1부터 n까지 정수의 합 구하기 1 (while)

print('1부터 n까지의 정수의 합을 구합니다.')
n = int(input('정수 입력: '))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지의 합계는 {sum}입니다.')