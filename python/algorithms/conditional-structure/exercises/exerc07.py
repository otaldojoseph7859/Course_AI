#
# 21
#
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 1.8

if celsius < 0:
    print("Freezing point")
else:
    print("Not freezing point")