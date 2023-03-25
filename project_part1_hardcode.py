print("Welcome to Circle Phones Profit calculator\n")
val = [120.45,99.50,75.69,65.73,51.49]
total = 0
product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
while (product_no != 0):
    if (product_no >0 and product_no <=5):
        qty = int(input("Enter quantity sold:\n "))
        total = total + val[product_no-1] * qty
    product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))


print("Your total profit for today is: ${}\n".format(total))

