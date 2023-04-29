#!/usr/bin/env python

# exercise 1
# open file and display all the content
with open('ex1.acc', 'r') as infile:
    for line in infile:
        print(line)

# exercise 2
# get filename from user
file = input('Insert filename: ')

# open the file and display the content
with open(file, 'r') as infile:
    for line in infile:
        print(line)

# ex 3
# get filename from user
file = input('Insert filename: ')

# open the file and count the number of lines
num = 0
with open(file, 'r') as infile:
    for line in infile:
        num += 1

print('The number of lines in this file is', num)

# ex 4
# get filename from user
file = input('Insert filename: ')

# open the file, change type of every line to float and count the sum of all lines
num = 0
with open(file, 'r') as infile:
    for line in infile:
        line = float(line)
        num += line

print('The sum of all lines is', num)

# ex 5
# get filename from user
file = input('Insert filename: ')

# open the file, count number of lines and sum of all lines
num_lines = 0
my_sum = 0
with open(file, 'r') as infile:
    for line in infile:
        num_lines += 1
        my_sum += float(line)

# display the average of all lines
print('The mean of all numbers in this file is', my_sum / num_lines)

# ex 6
# get filename from user
file = input('Insert filename: ')

# open the file and count lines with positive and negative numbers and zeroes
positive = 0
negative = 0
zeros = 0
with open(file, 'r') as infile:
    for line in infile:
        line = float(line)
        if line > 0:
            positive += 1
        elif line < 0:
            negative += 1
        else:
            zeros += 1

print('There are', positive, 'positive numbers.')
print('There are', negative, 'negative numbers.')
print('There are', zeros, 'zeros.')

# ex 7
# get filename from user
file = input('Insert filename: ')

# open the file and find largest number
max_num = float('-inf')
with open(file, 'r') as infile:
    for line in infile:
        if float(line) > max_num:
            max_num = float(line)

print('Maximum number is', max_num)

# ex 8
# get filename from user
file = input('Insert filename: ')

# open the file and find the smallest number
min_num = float('inf')
with open(file, 'r') as infile:
    for line in infile:
        if float(line) < min_num:
            min_num = float(line)

print('Minimum number is', min_num)

# ex 9
# get filename from user
file = input('Insert filename: ')

# initialize variables
positive = 0                # number of lines with positive value
negative = 0                # number of lines with negative value
zeros = 0                   # number of lines with zero
max_num = float('-inf')     # the largest number
min_num = float('inf')      # the smallest number
sum_all = 0                 # sum of all the numbers
num_lines = 0               # number of all lines in file

# open the file and find value of all the previous variables
with open(file, 'r') as infile:
    for line in infile:
        line = float(line)
        
        if line > 0:
            positive += 1
        elif line < 0:
            negative += 1
        else:
            zeros += 1
            
        if float(line) < min_num:
            min_num = float(line)
        if float(line) > max_num:
            max_num = float(line)

        sum_all += line
        num_lines += 1

# count the mean of all numbers in file        
mean = sum_all / num_lines

# display all the values with explenation
print('The sum of all lines is', num_lines)
print('The sum of all numbers is', sum_all)
print('The mean of all numbers is:', mean)

print('There are', positive, 'positive numbers.')
print('There are', negative, 'positive numbers.')
print('There are', zeros, 'zeros.')

print('Maximum number is', max_num)
print('Minimum number is', min_num)

# ex 10
import random

# initialize variables
get_it = ''     # test if pc got it
x = 1           # the smallest number pc can guess
y = 10          # the largest number pc can guess

print('''Please, answer just 'yes' and 'no'.''')

while get_it != 'yes':

    # end the while loop if game would not work properly
    if x > y:
        print('You should think a number between 1 and 10.')
        break

    # guess of number
    guess = random.randint(x, y)
    print('My guess is:', guess)
    get_it = input('Have I got it? ')

    # evaluation of user input
    if get_it == 'no':
        bigger = input('Is it greater than my guess? ')
        if bigger == 'yes':
            x = guess + 1
        elif bigger == 'no':
            y = guess - 1
        else:
            print('''Please, answer just 'yes' and 'no'.''')

    elif get_it == 'yes':
        print('I won!')
        
    else:
        print('''Please, answer just 'yes' and 'no'.''')