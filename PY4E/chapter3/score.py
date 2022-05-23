score = float(input('Enter Score: '))
if score > 1.0:
    print('Error: score range(0.0 ~ 1.0)');
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif (score > 0.6) and (score <= 0.0):
    print('F')
else:
    print('Enter the right Thing!')
