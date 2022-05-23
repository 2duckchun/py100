hrs = input('Enter hours: ')
payrate = input('Enter rate: ')
hours = float(hrs)
rate = float(payrate)

print((int(hours/40) - 1) * 40)

if hours <= 40:
    payment = hours * rate
    print(payment)

elif hours > 40:
    payment = (40 * rate) + (((int(hours/40) - 1) * 40) * (rate * 1.5)) + (int(hours % 40) * (rate * 1.5))
    print(payment)