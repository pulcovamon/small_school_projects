#!/usr/bin/env python

# ex 1-5

with open('sprot1.dat', 'r') as sprot_file:
    # initialize variables
    flag_sq = False     # variable for mark if program found the line with SQ
    seq_amino_acid = ''
    num_amino_acid = 0  # counting amino acids
    control_num = ''    # check if there is the right number of amino acids
    sprot_id = ''
    ac_number = ''      # accesion number

    for line in sprot_file:
        if flag_sq:
            for letter in line:
                # ord returns integer representating unicode character
                # (capital letters are between 65 and 90)
                if 65 <= ord(letter) <= 90:
                    seq_amino_acid += letter
                    num_amino_acid += 1
                # the sequence end with /
                elif letter == '/':
                    flag_sq = False

        elif line[:2] == 'ID':
            for i in range(2,len(line)):
                # there is always ' ' before ID
                if line[i] != ' ':
                    sprot_id += line[i]
                # it breakes the for loop if there is ' ' and the SwissProt ID is completed
                elif sprot_id != '':
                    break
            print('SwissProt ID is:', sprot_id)

            for i in range(len(line)):
                # there is always ; somewhere between the number of amino acids and
                # SwissProt ID that may also include some numbers
                # Read the line from the end
                if line[-i] == ';':
                    break
                # numbers are in unicode between 48 and 57
                elif 48 <= ord(line[-i]) <= 57:
                        control_num = line[-i] + control_num
            control_num = int(control_num)

        elif line[:2] == 'AC':
            for i in range(2, len(line)):
                # there is always ; after the accesion number
                if line[i] == ';':
                    break
                # there is always ' ' before ac
                elif line[i] != ' ':
                    ac_number += line[i]
            print('Accession number is:', ac_number)

        # set the flag on True if the sequence starts in the following line
        elif line[:2] == 'SQ':
            flag_sq = True

    print('The qmino acid sequence is:', seq_amino_acid)
    if control_num == num_amino_acid:
        print('Amino acid number check succesfull')

# ex 6

with open('sprot.fsa', 'w') as fsa_file:
    # header includes > and some specific signification, I use SwissProt ID
    header = '> ' + sprot_id + '\n'
    fsa_file.write(header)
    for i in range(len(seq_amino_acid)):
        fsa_file.write(seq_amino_acid[i])
        # after every 60th nucleotide make newline
        if (i+1) % 60 == 0:
            fsa_file.write('\n')

# ex 7

dna = ''
with open('dna.fsa', 'r') as dna_fsa_file:
    for line in dna_fsa_file:
        # skip the header that starts with >
        if line[0] != '>':
            # add the line without the newline character
            dna += line[:-1]

start_codons_pos = []
# end the for loop in the 3rd nucleotide from the end
for i in range(len(dna)-2):
    if dna[i:i+3] == 'ATG':
        # add the position to the list
        start_codons_pos.append(i+1)
        
print('List of positions of start codons ATG:', start_codons_pos)

# ex 8

flag_started = False
for i in range(len(dna)):
    if flag_started:
        # find stop codon that fits to the start (if I dewide it between codons)
        if (i-start+1) % 3 == 0 and dna[i:i+3] in ['TAA', 'TAG', 'TGA']:
            stop = i+1
            # stop looking for stop codons
            break
    
    # find the start codon and set the flag on True
    elif dna[i:i+3] == 'ATG':
        start = i+1
        flag_started = True

print('The fisrt start codon is on position', start, 'and the appropriate stop codon is in position', stop)

# ex 9

organism = input('Enter an organism in capital letters: ')

counter = 0      # count the lines that include the word from input

with open('orphans.sp', 'r') as sp_file:
    for line in sp_file:
        for i in range(len(line)-len(organism)):
            # there is always _ before the name of organism (it may include the word in other text)
            if line[i:i+len(organism)] == organism and line[i-1] == '_':
                counter += 1
print('There are', counter, organism, 'genes in this file')

# ex 10

# initialize variables
get_it = ''
x = 1           # the smallest number pc can guess
y = 10          # the largest number pc can guess

print('''Please, answer just 'yes' and 'no'.''')

while get_it != 'yes':

    # end the while loop if game would not work properly
    if x > y:
        print('You lie! You should think a number between 1 and 10.')
        break

    # guess of number

    guess = (y+x)//2
    if x == 9:
        guess = y

    print('My guess is:', guess)
    get_it = input('Have I got it? ')

    # evaluation of user input
    if get_it == 'no':
        bigger = input('Is it greater than my guess? ')
        if bigger == 'yes':
            x = guess
        elif bigger == 'no':
            y = guess
        else:
            print('''Please, answer just 'yes' and 'no'.''')

    elif get_it == 'yes':
        print('I won!')

    else:
        print('''Please, answer just 'yes' and 'no'.''')