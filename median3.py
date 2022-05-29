# 세 정수의 중앙값 구하기
def median(a, b, c):
    if a >= b:
        if b >= c: return b
        elif c >= a: return a
        else: return c
    else:
        if c >= b: return b
        elif a >= c: return a
        else: return c

try:
    f = int(input('첫 번째 정수의 입력값을 입력하세요 : '))
    s = int(input('두 번째 정수의 입력값을 입력하세요 : '))
    t = int(input('세 번째 정수의 입력값을 입력하세요 : '))

except:
    print('올바른 숫자를 입력하세요.')
    quit()

print(f'세 정수의 중간값은 {median(f, s, t)} 입니다!')
