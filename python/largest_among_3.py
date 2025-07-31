# Find the largest among 3 numbers using elif statement

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    print(a, "is the largest")
elif b > a and b > c:
    print(b, "is the largest")
else:
    print(c, "is the largest")