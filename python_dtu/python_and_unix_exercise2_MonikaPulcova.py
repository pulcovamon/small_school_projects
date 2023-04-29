#!/usr/bin/env python

# exercise 1
print('Hello World\n')

# exercise 2
for i in range(10):
    print('Hello World')

# exercise 3
for i in range(1,10):
    print(i)

# exercise 4
name = input('Type your name: ')

if name == 'Monika':
    print('Greetings, ', name, ', nice to meet you!')
else:
    print('Hi, ', name)

# exercise 5
num1 = float(input('Type a first number: '))
num2 = float(input('Type a second number: '))

print(num1, num2, num1 + num2, sep = '\n')

# exercise 6
num1 = float(input('Type a first number: '))
num2 = float(input('Type a second number: '))
operator = input('Type an operation (+, -, * or /): ')

if operator == '+':
    print(num1, '+', num2, '=', num1 + num2)
elif operator == '-':
    print(num1, '-', num2, '=', num1 - num2)
elif operator == '*':
    print(num1, '*', num2, '=', num1 * num2)
else:
    print(num1, '/', num2, '=', num1 / num2)

# exercise 7
num1 = int(input('Type a first integer: '))
num2 = int(input('Type a second integer (greater than first integer): '))

for i in range(num1, num2+1):
    print(i)

# exercise 8
num1 = int(input('Type a first integer: '))
num2 = int(input('Type a second integer: '))

if num1 <= num2:
    for i in range(num1, num2+1):
        print(i)
else:
    for i in range(num2, num1+1):
        print(i)

# exercise 9
num1 = float(input('Type a number: '))
num2 = num1

while num2 >= num1:
    num1 = num2
    num2 = float(input('Type a number: '))

# exercise 10
num = int(input('Type a positive integer: '))

if num > 0:
    fac = 1
    for i in range(1, num + 1):
        fac *= i
    print(fac)
else:
    print('ERROR, integer must be positive!\n')

# exercise 11
num = int(input('Type an integer: '))

result = 0

if num >= 0:
    for i in range(num+1):
        result += i
else:
    for i in range(num, 1):
        result += i

print(result)
