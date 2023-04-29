#!/usr/bin/env python

# ex1

flag = True

with open('words.txt', 'w') as txt_file:
    while flag:
        word = input('''Enter some word you want to save (or 'stop' if you want to finish): ''')
        if word == 'stop':
            flag = False
        else:
            # add newline character and write the word into the file
            word += '\n'
            txt_file.write(word)

# ex 2

# make an emty list
words_list = []

with open('words.txt', 'r') as txt_file:
    for line in txt_file:
        # take line without newline charater and add it into the list
        line = line[:-1]
        words_list.append(line)

# sort the first word alphabetically
words_list[0] = ''.join(sorted(words_list[0]))
words_list.reverse()

print(words_list)

# ex 3

# make an empty list for accession numbers
genbank_ac_list = []

with open('ex5.acc', 'r') as acc_file:
    for line in acc_file:
        # add te accession number only if it is unmatched
        if line not in genbank_ac_list:
            # add line without the new line character
            line = line[:-1]
            genbank_ac_list.append(line)

genbank_ac_list.sort()

with open('clean.acc', 'w') as acc_write_file:
    for accession_num in genbank_ac_list:
        # wirte all the found accession numbers to the file and add newline character
        acc_write_file.write(accession_num)
        acc_write_file.write('\n')

# ex 4

# sort the gen bank list alphabetically
genbank_ac_list.sort()
i = 0
while i < (len(genbank_ac_list)-1):
    if genbank_ac_list[i] == genbank_ac_list[i+1]:
        # pop the following list item
        genbank_ac_list.pop(i+1)
    # go to the following iteration only when not popping any item
    else:
        i = i+1

# ex 5

flag = True

while flag:
    accession_num = input('Enter accession number you want to find or write STOP: ')
    # stop searching accession numbers
    if accession_num == 'STOP':
        flag = False
        break
    i = 0
    # linear searching - from the first item to the last
    while i <= len(genbank_ac_list)-1:
        if genbank_ac_list[i] == accession_num:
            print('FOUND in position:', i+1)
            break
        # when it is on the last item and there is not the accession number
        elif i == len(genbank_ac_list)-1:
            print('NOT FOUND')
        i += 1

# ex 6

accession_num = input('Enter accession number you want to find: ')

found = False
# define the limits of searched interval
start = 0
stop = len(genbank_ac_list)

while not found:

    # update the limits - right in the middle of the interval
    my_index = (stop - start)//2 + start

    if genbank_ac_list[my_index] == accession_num:
        found = True

    # reduce the interval (only the lower half)
    elif genbank_ac_list[my_index] > accession_num:
        stop = my_index

    # only the upper half
    else:
        start = my_index

print('found on line', my_index)

# ex 8

collumn2 = []

numbers = ['0','1','2','3','4','5','6','7','8','9','.','-']

with open('ex1.dat', 'r') as dat_file:
    for line in dat_file:
        word = ''
        flag = False
        for letter in line:
            if flag:
                # if finds the second space
                if letter not in numbers:
                    flag = False
                    break
                # make the whole word
                word += letter
            # it finds the first space and sets the flag to true
            elif letter not in numbers:
                flag = True
            collumn2.append(word)

print(collumn2)

# ex 9

my_sum = 0

# define list of characters used in numbers
numbers = ['0','1','2','3','4','5','6','7','8','9','.','-']

with open('ex1.dat') as dat_file:
    for line in dat_file:
        word = ''
        for letter in line:
            # if the character is not space, add it to the end of variable word
            # I tried to do it with "if letter != ' '" but it did not work
            if letter in numbers:
                word += letter
                # if it is space, convert the word to number and add it to the sum
            else:
                my_sum += float(word)
                word = ''

print('the sum of all the lines is', my_sum)

# ex 10

# define list of characters used in numbers
numbers = ['0','1','2','3','4','5','6','7','8','9','.','-']

# define an emty list
sum_list = []

with open('ex1.dat') as dat_file:
    for line in dat_file:
        word = ''
        # counter of columns
        counter = 0
        for letter in line:
            # if the character is not space, add it to the end of variable word
            if letter in numbers:
                word += letter
                # if it is space, convert the word to number and add it to the sum
            else:
                counter += 1
                # make the apropriate number of items in the list
                if counter > len(sum_list):
                    # if there are more column than items is the list add on item
                    sum_list.append(0)
                sum_list[counter-1] += float(word)
                word = ''

print('there are', len(sum_list), 'columns and their sums are:', sum_list)