smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif smallest > value :
        smallest = value
    print(smallest, value)
print('After', smallest)


# None 타입 : 단 하나의 값만 가짐. 상수.
# 공백을 사용하기 위해 사용함. marker, flag ~
# if is