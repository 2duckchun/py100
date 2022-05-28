purse = dict() # 또는 purse = {}
purse['money'] = 12 # money라는 키에 12라는 값 연결
purse['candy'] = 3 # candy라는 키에 3이라는 값 연결
purse['tissues'] = 75 # tissues라는 키에 75라는 값 연결

print(purse)
print(purse['tissues'])
purse['candy'] = purse['candy'] + 99
print(purse)
print(purse[0])