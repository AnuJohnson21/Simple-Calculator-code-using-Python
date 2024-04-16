
print('Simple Calculator')
num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))

print('1. +')
print('2. -')
print('3. *')
print('4. /')
op=input('select the operator:')

if(op=='+'):
    print(num1, '+', num2, '=', num1+num2)
if(op=='-'):
    print(num1, '-', num2, '=', num1-num2)
if(op=='*'):
    print(num1, '*', num2, '=', num1*num2)
if(op=='/'):
    if (num1 == 0) or (num2 == 0):
        print('Cannot divide by zero, enter valid data')
    else:
        print(num1, '/', num2, '=', num1/num2)


