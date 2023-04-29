#!/usr/bin/env python
'''
# ex 1
import sys

# get two numbers from user and count the mean
try:
    num1 = float(input('Type first number: '))
    num2 = float(input('Type second number: '))
    mean = int((num1 + num2) / 2)
# end the program with exit status 1 if user input is not a number
except ValueError:
    print('Hey, that was not a number!')
    sys.exit(1)

print('The mean of', num1, 'and', num2, 'rounded to integer is', mean)

# ex 3
# initialize counter of negatives numbers
negative = 0

# open the file, find numbers and compare if there are smaller than zero
with open('ex1.dat', 'r') as dat_file:
    for line in dat_file:
        for char in line:
            if char == '-':
                negative += 1

print('There are', negative, ' negative numbers in the file.')

# ex 4
# ask user for input in a certain format
temp1 = input('Please, enter a temperature in format 15C for celsius or 15F in farenheit: ')

# find the unit of temperature and convert it into the other
if temp1[-1] == 'C':
    temp2 = float(temp1[:-1]) * 9/5 + 32
    unit = 'F'
elif temp1[-1] == 'F':
    temp2 = float(temp1[:-1]) * 9/5 - 32
    unit = 'C'
# in case of user input in bad format raise error
else:
    raise ValueError

print(temp1, '=', temp2, unit)
print('\n')

# ex 5
from os import write
# make epmty list
accession_numbers = []
with open('orphans.sp', 'r') as sp_file:
    for line in sp_file:
        # initialize variables for every line
        accession_num = ''
        marker = False
        for letter in line:
            if marker == True:
                # save the number into variable
                accession_num += letter
                # find the end of the number by indexing
                if len(accession_num) > 5:
                    if accession_num[-5:] == 'CDS.1':
                        accession_numbers.append(accession_num)
                        marker = False
            # find the start of the number
            elif letter == '>':
                marker = True

with open('accesion_numbers.txt', 'w') as txt_file:
    for number in accession_numbers:
        txt_file.write(number)
        txt_file.write('\n')
    print('Done')

# ex 7
# initialize variable as empty string
dna_former = ''
with open('dna.dat', 'r') as dat_file:
    for line in dat_file:
        dna_former += line
# make dictionary for complementary nucleotides
complementaries={'A':'T','C':'G','T':'A','G':'C'}
dna_new=''
# skip newline characters
for nucleotide in dna_former:
    if nucleotide == '\n':
        continue
    # make new variable
    dna_new += complementaries[nucleotide]

print(dna_new)

# ex 8
# reverse the string using string indexing
dna_reverse = dna_new[-1:0:-1]

print(dna_reverse)

# ex 9
# make new file and write into it the DNA sequence
with open('revdna.dat', 'w') as dna_outfile:
    for i in range(len(dna_reverse)):
        dna_outfile.write(dna_reverse[i])
        # make newline after every 60th nucleotide
        if (i+1) % 60 == 0:
            dna_outfile.write('\n')
'''

# ex 10
# initialize variable as empty string
dna_former = ''
# make dictionary for complementary nucleotides
complementaries={'A':'T','C':'G','T':'A','G':'C'}
dna_new = ''

with open('dna.fsa', 'r') as fsa_file:
    for line in fsa_file:
        if line[0] == '>':
            name = line
            continue
        else:
            dna_former += line
for nucleotide in dna_former:
    if nucleotide == '\n':
        continue
    # make new variable
    dna_new += complementaries[nucleotide]

with open('revdna.dat', 'w') as outfile:


# ex 11
# initialize the variables
a_sum = 0
t_sum = 0
c_sum = 0
g_sum = 0

with open('dna.fsa', 'r') as fsa_file:
    for line in fsa_file:
        # skip the line with the name of dna
        if line[0] == '>':
            continue
        for letter in line:
            if letter == 'A':
                a_sum += 1
            elif letter == 'T':
                t_sum += 1
            elif letter == 'C':
                c_sum +=1
            elif letter == 'G':
                g_sum += 1

print('The number of A is', a_sum)
print('The number of T is', t_sum)
print('The number of C is', c_sum)
print('The number of G is', g_sum)

if coffeeEmpty == true:
    print('I need more coffee!')
    RefillCoffee()
else:
    DrinkCoffee()