#
# 
#
try:
    number = int(input(""))
    print(f"You type: {number}")

except ValueError:
    print("ERROR: You not type a integer number")

#
#
#
try:
    num_str = input("Type a number: ")
    num_int = int(num_str)
    result = 10 / num_int
    print(f"10 divided by {num_int} ie {result}")

except ValueError:
    print(f"ERROR: You not type a number")

except ZeroDivisionError:
    print(f"ERROR: Can't divide by zero")

except Exception as e:
    print(f"ERROR: An unexpected error occurred {e}")

# Só é executado se não ocorrernenhum erro!
else:
    print("Ok!")

# Executa mesmo que tenha erro no try
finally:
    num_str = input("Type a number: ")
    
#
#
#
file = None

try: 
    file = open("data.txt", "r")
    content = file.read()
    print("File read successfully")

except FileNotFoundError:
    print("ERROR: File not found")

except Exception as e:
    print(f"ERROR: error reading file {e}")

else:
    print("File processing completed successfully")

finally:
    if file:
        file.close()
        print("File closed")