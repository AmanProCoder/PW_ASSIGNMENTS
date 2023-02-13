CostPrice=float(input("Enter the cost price:"))
if(CostPrice>100000):
    print("15%")
elif CostPrice>50000:
    print("10%")
else:
    print("5%")