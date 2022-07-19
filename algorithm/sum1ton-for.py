# 1부터 n까지 정수의 합 구하기 1 (for)

print('1부터 n까지의 정수의 합을 구합니다.')
n = int(input('정수 입력: '))

sum = 0
for i in range(1, n + 1): # 마지막 인덱스는 n번째가 빠지니 +1을 해줌.
    sum += i

print(f'1에서 {n}까지 정수의 합은 {sum}입니다.')