# 세 정수를 입력받아 최댓값 구하기
print('세 정수의 최댓값을 구합니다.')
try:
    a = int(input('첫 번째 정수의 입력값을 입력하세요 : '))
    b = int(input('두 번째 정수의 입력값을 입력하세요 : '))
    c = int(input('세 번째 정수의 입력값을 입력하세요 : '))

except:
    print('올바른 숫자를 입력하세요.')
    print('프로그램을 종료합니다.')
    quit()

max = a
if b > max: max = b
if c > max: max = c

print(f'최댓값은 {max} 입니다.')