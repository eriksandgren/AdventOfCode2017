#!/usr/bin/env python
import sys

stepSize = 348

def part1():
  circBuf = [0]
  listLen = 1
  currentPosition = 0
  for elem in xrange(1, 2018):
    insertPosition = ((currentPosition + stepSize) % listLen) + 1
    circBuf.insert(insertPosition, elem)
    listLen += 1
    currentPosition = insertPosition

  print "Part 1 answer", circBuf[currentPosition + 1]

def part2():
  listLen = 1
  currentPosition = 0
  afterZero = None
  for elem in xrange(1, 50000001):
    insertPosition = ((currentPosition + stepSize) % listLen) + 1
    if insertPosition == 1:
      afterZero = elem
    listLen += 1
    currentPosition = insertPosition

  print "Part 2 answer", afterZero

part1()
part2()