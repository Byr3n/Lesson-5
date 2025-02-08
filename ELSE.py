actual_cost=float(input("Enter the actual product:"))
sale_amount=float(input("Enter the sales amount:"))
if sale_amount>actual_cost:
    amount=sale_amount-actual_cost
    print("Total profit={0}".format(amount))
else:
    print("no profit")
