#!/usr/bin/env python

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()

    myInput = myInput.split('\n')
    return myInput
def part1():
  s = parseInput()
  myInput = [int(x) for x in s]
  maxInd = len(myInput) - 1
  ind = 0
  steps = 0
  while ind <= maxInd and ind >= 0:
    steps += 1
    newInd = ind + myInput[ind]
    myInput[ind] += 1
    ind = newInd
  print steps 
 
def part2():
  s = parseInput()
  myInput = [int(x) for x in s]

  maxInd = len(myInput) - 1
  ind = 0
  steps = 0
  while ind <= maxInd and ind >= 0:
    steps += 1
    offset = myInput[ind]
    newInd = ind + offset
    if offset >= 3:
      myInput[ind] -= 1
    else:
      myInput[ind] += 1
    ind = newInd

  print steps 
 
 
part1()
part2()