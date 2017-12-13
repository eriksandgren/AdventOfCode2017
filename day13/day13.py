#!/usr/bin/env python

s = """ 
0: 3
1: 2
4: 4
6: 4
""".strip()

s = """ 
0: 5
1: 2
2: 3
4: 4
6: 6
8: 4
10: 6
12: 10
14: 6
16: 8
18: 6
20: 9
22: 8
24: 8
26: 8
28: 12
30: 12
32: 8
34: 8
36: 12
38: 14
40: 12
42: 10
44: 14
46: 12
48: 12
50: 24
52: 14
54: 12
56: 12
58: 14
60: 12
62: 14
64: 12
66: 14
68: 14
72: 14
74: 14
80: 14
82: 14
86: 14
90: 18
92: 17
""".strip()

class Layer():
  def __init__(self, level, range_):
    self.level = level
    self.range = range_
    self.scanner_pos = 0

  def display(self):
    print "Level", self.level, "Range", self.range
  
  def calcScannerPosInPicoSecond(self, ps):
    pos = ps % (self.range * 2 - 2)
    if pos >= self.range:
      pos = self.range - 1 - (pos % (self.range -1 ))
    return pos
      
def part1():
  input_l  = s.split('\n')
  layers_l = []
  for l in input_l:
    layers_s = l.split(': ')
    layers_l.append(Layer(int(layers_s[0]), int(layers_s[1])))

  severity = 0
  for lay in layers_l:
    pos = lay.calcScannerPosInPicoSecond(lay.level)
    if pos is 0:
      severity += lay.level * lay.range

  print "Severity:", severity


def checkIfCaught(layers_l, delay):
  for lay in layers_l:
    pos = lay.calcScannerPosInPicoSecond(lay.level + delay)
    if pos is 0:
      return True
  return False

def part2():
  input_l  = s.split('\n')
  layers_l = []
  for l in input_l:
    layers_s = l.split(': ')
    layers_l.append(Layer(int(layers_s[0]), int(layers_s[1])))

  delay = 0
  while checkIfCaught(layers_l, delay):
    delay += 1
  
  print "Delay in picoseconds to not get caught", delay



part1()
part2()
