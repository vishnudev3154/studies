#sum of n numbers
firstNumber = int(input('enter a first number:'))
secondNumber = int(input('enter a second number:')) 
sum = 0
for i in range(firstNumber, secondNumber +1):
    sum = sum + i
print('sum',sum)

