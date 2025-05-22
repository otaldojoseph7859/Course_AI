#
# 
#
value = []
while True:
    number = int(input("Enter a number or 0 to close program: "))
    if number == 0:
        print("Close program...")
        break
    value.append(number)
    print("List: ", value)
    print("List: ", sorted(value))