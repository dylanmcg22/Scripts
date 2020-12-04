region = "West"
annualSales = 500000
firstName = "Tony"

if annualSales >= 500000:
    print("Gold Customer")
elif annualSales >= 300000:
    print("Silver Customer")
elif annualSales >= 100000:
    print("Bronze Customer")
    
print("Thank you for your business")
print(f"Your sales representative is {firstName}," \
" you are in the {region}," \
" and you had {annualSales} in the sales last year. Thanks!")
