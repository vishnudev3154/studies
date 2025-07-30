#sum of odd numbers
firstNumber = int(input('enter a first number:'))
secondNumber = int(input('enter a second number:'))
sum = 0
for i in range(firstNumber, secondNumber + 1):
    if i % 2 != 0:
        sum = i
print('sum of odd numbers:', sum)