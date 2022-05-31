# range(), step 실습

n = int(input('정수를 입력하세요: '))

sum = 0

for i in range(1, n, 2):
    sum += i

print(f'1부터 {n}까지의 정수의 합 : {sum}')