#!/usr/bin/env python
import sys

def parseInput():
    file = open("input.txt")
    return file.readline()[:-1]  # Skip the \n at the end..

def part1():
    my_input = parseInput()
    prev = my_input[-1]
    result = 0
    for char in my_input:
        if char == prev:
            result += int(char)    
        prev = char
    print result

def part2():
    my_input = parseInput()
    k = int(len(my_input) / 2)
    my_input_twice = my_input + my_input
    result = 0
    for i, char in enumerate(my_input):
        if char == my_input_twice[i + k]:
            result += int(char)    
    print result

part1()
part2()

