# Electricity bill calculator based on unit slabs

units = int(input("Enter number of units consumed: "))
bill = 0

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + ((units - 200) * 10)

print("Total bill is: ", bill)