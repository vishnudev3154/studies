# Road tax calculator based on bike cost price

cost_price = float(input("Enter the cost price of the bike (in Rs): "))

if cost_price > 100000:
    tax = cost_price * 0.15
elif cost_price > 50000:
    tax = cost_price * 0.10
else:
    tax = cost_price * 0.05

print("Road tax to be paid (in Rs):", tax)