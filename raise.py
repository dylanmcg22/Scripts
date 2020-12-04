a = float(input("Enter a number. "))
b = float(input("Enter a number to divide by. "))

try:
    print(f"The answer is {a/b}.")
except:
    if b==0:
        raise
        print("This did not work. ")
else:
    print("You sucessfully used the divison feature in Python.")
finally:
    print("Thank you for playing.")