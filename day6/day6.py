#!/usr/bin/env python
import operator


def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    myInput = myInput.split('\t')
    return myInput

def redistribute(state):
  index, blocksToDistribute = max(enumerate(state), key=operator.itemgetter(1))
  state[index] = 0
  numBlocks = len(state)
  while blocksToDistribute != 0:
    index = (index + 1) % (numBlocks)
    blocksToDistribute -= 1
    state[index] += 1    
  
  return state

def part1():
  s = parseInput()
  state = [int(x) for x in s]

  previous_states = []
  redistributionCount = 0
  while state not in previous_states:
    previous_states.append(state) 
    state = redistribute(list(state))
    redistributionCount += 1
  print redistributionCount
  print len(previous_states)

def part2():
  s = parseInput()
  state = [int(x) for x in s]

  previous_states = []
  redistributionCount = 0
  while state not in previous_states:
    previous_states.append(state) 
    state = redistribute(list(state))
    redistributionCount += 1
  
  previous_states = []
  redistributionCount = 0
  while state not in previous_states:
    previous_states.append(state) 
    state = redistribute(list(state))
    redistributionCount += 1

  print redistributionCount
  print len(previous_states)
part1()
part2()