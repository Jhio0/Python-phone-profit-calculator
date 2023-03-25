print("Welcome to Circle Phones Profit calculator\n")
val = [120.45,99.50,75.69,65.73,51.49]
val1 = []
while True:
        profit = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
        if profit == 1:
            val2 = val[0]
            quantity = int(input("Enter quantity sold:\n "))
            val3 = quantity * val2
            val1.append(val3)
        elif profit == 2:
            val2 = val[1]
            quantity = int(input("Enter quantity sold:\n "))
            val3 = quantity * val2
            val1.append(val3)
        elif profit == 3:
            val2 = val[2]
            quantity = int(input("Enter quantity sold:\n "))
            val3 = quantity * val2
            val1.append(val3)
        elif profit == 4:
            val2 = val[3]
            quantity = int(input("Enter quantity sold:\n "))
            val3 = quantity * val2
            val1.append(val3)
        elif profit == 5:
            val2 = val[4]
            quantity = int(input("Enter quantity sold:\n "))
            val3 = quantity * val2
            val1.append(val3)
        elif profit == 0:
            break
        else:
            print("that is not one of the values")

x = sum(val1)
print("Your total profit for today is: ${}\n".format(x))

