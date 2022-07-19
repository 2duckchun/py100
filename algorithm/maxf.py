# 세 정수의 최댓값 구하기 함수
def max3(a, b, c):
    max = a
    if b > max : max = b
    if c > max : max = c
    return max

f = int(input('첫 번째 정수를 입력하세요: '))
s = int(input('두 번째 정수를 입력하세요: '))
t = int(input('세 번째 정수를 입력하세요: '))

print(f'최대 값은 {max3(f, s, t)} 입니다!')