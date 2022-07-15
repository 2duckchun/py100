a = { 'apple', 'lemon', 'banana' }
a.update({'kiwi', 'banana'}) # 사과 레몬 바나나 키위
a.remove('lemon') # 사과 바나나 키위
a.add('apple')
for i in a:
    print(i)