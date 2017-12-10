#!/usr/bin/env python

def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    return myInput

def part1():
  input_str = parseInput()[:-1]
  print input_str

  garbage = False
  score = 0
  current = 0
  garbageCnt = 0
  skip = False
  for c in input_str:
    print c
    if garbage:
      if skip:
        skip = False
        continue
      if c == '!':
        skip = True 
      elif c == '>':
        garbage = False
      else:
        garbageCnt += 1

    else:
      if c == '{':
        current += 1
      elif c == '}':
        score += current
        current -= 1
      elif c == '<':
        garbage = True

  print score, garbageCnt
part1()
