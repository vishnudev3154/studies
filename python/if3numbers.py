firstNumber = int(input('enter first numbrer :'))
secondNumber = int(input('enter second number:'))
tirdNumber = int(input('enter third number:'))
if firstNumber > secondNumber:
    if firstNumber > tirdNumber:
        print(firstNumber, 'is greater')
    else:
        print(tirdNumber, 'is greater')
else:
    if secondNumber > tirdNumber:
        print(secondNumber, 'is greater')
    else:
        print(tirdNumber, 'is greater')