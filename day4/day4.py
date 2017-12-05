#!/usr/bin/env python
import sys

def part1():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()

    myInput = myInput.split('\n')
    print myInput
    numPassphrases = 0
    for line in myInput:
        words_l = line.split()
        if (len(set(words_l)) == len(words_l)):
            numPassphrases += 1
    
    print numPassphrases
 
def part2():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()

    myInput = myInput.split('\n')
    numPassphrases = 0
    for line in myInput:
        words_l = line.split()
        sorted_words_l = []
        for word in words_l:
            sorted_words_l.append(''.join(sorted(word)))
    
        if (len(set(sorted_words_l)) == len(sorted_words_l)):
            numPassphrases += 1
    
    print numPassphrases
 
part1()
part2()

