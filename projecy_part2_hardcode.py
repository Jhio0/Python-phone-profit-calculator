print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by\nweek or you can divide the week into weekdays and the weekend.\n")
print("Welcome to Circle Phones Profit calculator\n")
pr3 =("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend\n")
print(pr3)
pr1 =("Enter:\n 1 - For specific Day \n 2 - For the Week\n 3 - For Week Business Days \n 4 - For Weekend days\n 0 - Exit")
print(pr1)
pr2 =("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")

while True:
    #TEST 1 CODE
    #Days code for speicifc type of day
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday" ]
    enter_val = int(input())
    if enter_val == 1:
        print(pr2)
        day_val = str(input())
        if day_val in days:
            print("For {}".format(day_val))
        else:
            print("Wrong days")
            break
        val = [120.45,99.50,75.69,65.73,51.49]
        total = 0
        product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
        while (product_no != 0):
            if (product_no >0 and product_no <=5):
                qty = int(input("Enter quantity sold:\n "))
                total = total + val[product_no-1] * qty
                product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
        
        print(f"Your total profit for the week is: ${total:.2f}\n")
        print("More hard work needed... The last {} wasn't the best\n".format(day_val))
        print(pr3)
        print(pr1)

    #TEST 2 CODE
    elif enter_val == 2:
        val = [120.45,99.50,75.69,65.73,51.49]
        total = 0
        for x in days:#All of the days
            print("For {}".format(x))
            product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
            while (product_no != 0):
                if (product_no >0 and product_no <=5):
                    qty = int(input("Enter quantity sold:\n "))
                    total = total + val[product_no-1] * qty
                    product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))

        print(f"Your total profit for the week is: ${total:.2f}\n")
        if total <= 10000:
            print("“We didn't reach our goal for this period. More work is needed.”\n")
        elif total >= 10000:
            print("You did good this week\n")
        print(pr3)
        print(pr1)

    #TEST 3 CODE
    elif enter_val == 3:#Week days
        val = [120.45,99.50,75.69,65.73,51.49]
        total = 0
        for x in days[:5]:
            print("For {}".format(x))
            product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
            while (product_no != 0):
                if (product_no >0 and product_no <=5):
                    qty = int(input("Enter quantity sold:\n "))
                    total = total + val[product_no-1] * qty
                    product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))

        print(f"Your total profit for the week (bussiness days): ${total:.2f}\n")
        if total <= 10000:
            print("“We didn't reach our goal for this period. More work is needed.”\n")
        elif total >= 10000:
            print("You did good this week (business days)\n")
        print(pr3)
        print(pr1)
    
    #TEST 4 CODE
    elif enter_val == 4:#Week ends
        val = [120.45,99.50,75.69,65.73,51.49]
        total = 0
        for x in days[5:7]:
            print("For {}".format(x))
            product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
            while (product_no != 0):
                if (product_no >0 and product_no <=5):
                    qty = int(input("Enter quantity sold:\n "))
                    total = total + val[product_no-1] * qty
                    product_no = int(input("Enter product number 1-5, or enter 0 to stop:\n "))

        print(f"Your total profit for the weekend: ${total:.2f}\n")
        if total <= 10000:
            print("“We didn't reach our goal for this period. More work is needed.”\n")
        elif total >= 10000:
            print("You did good this weekend\n")
        print(pr3)
        print(pr1)

















































