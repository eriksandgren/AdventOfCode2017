#!/usr/bin/env python
from collections import deque
import sys

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()

    myInput = myInput.split(',')
    return myInput

def part1():
  line = []
  myInput = parseInput()
  for i in range(ord('a'), ord('p')+1):
    line.append(chr(i))

  line = deque(line)
  for ind, com in enumerate(myInput):
    if com[0] == 's':
      num = int(com[1:])
      line.rotate(num)
    elif com[0] == 'x':
      ind1, ind2 = [int(x) for x in com[1:].split('/')]
      line[ind1], line[ind2] = line[ind2], line[ind1]
    elif com[0] == 'p':
      prog1, prog2 = [x for x in com[1:].split('/')]
      for ind, p in enumerate(line):
        if p == prog1:
          line[ind] = prog2
        if p == prog2:
          line[ind] = prog1
    else:
      assert(False)

  print "Arrangement after one dance", ''.join(line)

def part2():
  line = []
  myInput = parseInput()
  for i in range(ord('a'), ord('p')+1):
    line.append(chr(i))
  line = deque(line)
  seenArrangements = []
  numDances = 0
  while numDances < 1000000000:
    arrangement = ''.join(line)
    if arrangement in seenArrangements:
      print seenArrangements
      finalPos = 1000000000 % len(seenArrangements)
      print "Arrangements cyclic with cycle length", len(seenArrangements)
      print "Final arrangement after 1000000000 dances", seenArrangements[finalPos]
      sys.exit()
    seenArrangements.append(arrangement)
    for ind, com in enumerate(myInput):
      if com[0] == 's':
        num = int(com[1:])
        line.rotate(num)
      elif com[0] == 'x':
        ind1, ind2 = [int(x) for x in com[1:].split('/')]
        line[ind1], line[ind2] = line[ind2], line[ind1]
      elif com[0] == 'p':
        prog1, prog2 = [x for x in com[1:].split('/')]
        for ind, p in enumerate(line):
          if p == prog1:
            line[ind] = prog2
          if p == prog2:
            line[ind] = prog1
      else:
        assert(False)
    numDances += 1

part1()
part2()