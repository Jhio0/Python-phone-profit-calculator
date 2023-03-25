print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by\nweek or you can divide the week into weekdays and the weekend.\n")
print("Welcome to Circle Phones Profit calculator\n")
pr3 =("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend\n")
print(pr3)
pr1 =("Enter:\n 1 - For specific Day \n 2 - For the Week\n 3 - For Week Business Days \n 4 - For Weekend days\n 0 - Exit")
print(pr1)
pr2 =("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")

while True:
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday" ]
    enter_val = int(input())
    if enter_val == 1:
        print(pr2)
        day_val = input()
        print("For {}".format(day_val))
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

        x = round(sum(val1), 2)
        print("Your total profit for today is: ${}\n".format(x))
        print("More hard work needed... The last {} wasn't the best\n".format(day_val))
        print(pr3)
        print(pr1)

    elif enter_val == 2:
        val = [120.45,99.50,75.69,65.73,51.49]
        val1 = []
        for x in days:
            print("For {}".format(x))
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
        y = round(sum(val1), 2)
        print("Your total profit for the week is: ${}\n".format(y))
        if y <= 10000:
            print("“We didn't reach our goal for this period. More work is needed.”\n")
        elif y >= 10000:
            print("You did good this week\n")
        print(pr3)
        print(pr1)

    elif enter_val == 3:
        val = [120.45,99.50,75.69,65.73,51.49]
        val1 = []
        for x in days[:5]:
            print("For {}".format(x))
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
        y = round(sum(val1), 2)
        print("Your total profit for the week (business days) is: ${}\n".format(y))
        if y <= 10000:
            print("“We didn't reach our goal for this period. More work is needed.”t\n")
        elif y >= 10000:
            print("You did good this week (business days)\n")
        print(pr3)
        print(pr1)

    elif enter_val == 4:
        val = [120.45,99.50,75.69,65.73,51.49]
        val1 = []
        for x in days[5:7]:
            print("For {}".format(x))
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
        y = round(sum(val1), 2)
        print("Your total profit for the week is: ${}\n".format(y))
        if y <= 10000:
            print("“We didn't reach our goal for this period. More work is needed.”\n")
        elif y >= 10000:
            print("You did good this week\n")
        print(pr3)
        print(pr1)


























































