def subtotal(orderAmt, salesTax):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal


firstOrderTotal = subtotal(300, .08)
secondOrderTotal = subtotal(400, .06)

thirdOrderAmount = input("What was the order amount? ")
thirdTax = input("Enter your Sales tax rate.")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

print("Your subtotal for the first order is % .2f" %firstOrderTotal) # % refers to firstOrderTotal, second and third
print("Your subtotal for the second order is % .2f" %secondOrderTotal) #  % .2f format to two decimal places
print("Your subtotal for the third order is % .2f" %thirdOrderTotal)