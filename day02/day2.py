#!/usr/bin/env python
import sys

def findLargestDiffInRow(row):
    small = min(row)
    large = max(row)
    return large - small

def parseInput():
    mat = []
    with open('input.txt') as f:
        for line in f:
            data = [int(x) for x in line.split()]
            mat.append(data)
    return mat

def part1():
    mat = parseInput()
    checksum = 0
    for row in mat:
        checksum += findLargestDiffInRow(row)

    print checksum

def checkIfNumberIsDivisible(row, num, ind):
    for index, number in enumerate(row):
        if index == ind:
            continue
        if (num % number) == 0:
            return num / number
    return 0

def findEvenlyDivisibleDivision(row):
    for ind, num in enumerate(row):
        division = checkIfNumberIsDivisible(row, num, ind)
        if (division is not 0):
            return division
    return 0

def part2():
    mat = parseInput()
    checksum = 0
    for row in mat:
        checksum += findEvenlyDivisibleDivision(row)
    print checksum

part1()
part2()