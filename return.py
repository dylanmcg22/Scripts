def subtotal(orderAmt, salesTax=.08):
    subtotal = float(orderAmt) * (1 + float(salesTax))
    return subtotal

def orderMsg():
    print("Thank you for your order(s)")
    return


firstOrderTotal = subtotal(300)
secondOrderTotal = subtotal(400, .06)

thirdOrderAmount = input("What was the order amount? ")
thirdTax = input("Enter your Sales tax rate.")
thirdOrderTotal = subtotal(thirdOrderAmount, thirdTax)

fourthOrderTotal = subtotal(800)


print("Your subtotal for the first order is % .2f" %firstOrderTotal) # % refers to firstOrderTotal, second and third
print("Your subtotal for the second order is % .2f" %secondOrderTotal) #  % .2f format to two decimal places
print("Your subtotal for the third order is % .2f" %thirdOrderTotal)
print("Your subtotal for the fourth order is % .2f" %fourthOrderTotal)