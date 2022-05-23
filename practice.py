x = float(input("Enter Hours: "))
y = float(input("Enter Rate: "))

if x <= 40:
    print("Pay: ", x * y)

elif x > 40:
    print("Pay: ", 40 * y + (x - 40) * 1.5 * y)
