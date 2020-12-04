import sys
a = float(input("Enter a number. "))
b = float(input("Enter a number to divide by. "))

try:
    print(f"The answer is {a/b}.")
except:
    print(sys.exc_info()[0])
    print("This did not work. Did you try to divide by zero?")
else:
    print("You sucessfully used the divison feature in Python.")
finally:
    print("Thank you for playing.")