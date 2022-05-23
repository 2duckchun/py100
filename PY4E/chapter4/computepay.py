def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        otp = (hours - 40) * (rate * 0.5)
        return reg + otp
    else:
        pay = hours * rate
        return pay
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
print('Pay', computepay(hours, rate))