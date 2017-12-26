#!/usr/bin/env python
import sys

from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

s = """ 
set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
""".strip()

class Program():
  def __init__(self, programId, registers_l, in_l):
    self.id = programId
    self.mult_count = 0
    self.instruction_index = 0
    self.registers = {}
    self.registers_l = registers_l
    self.in_l = in_l
    for reg in registers_l:
      self.registers[reg] = 0
    self.registers['p'] = programId
    self.friend = None
    self.message_queue = []
    self.waiting = False

  def setRegister(self, reg, val):
    self.registers[reg] = val

  def isNotWaiting(self):
    return not self.waiting

  def setFriend(self, friendProgram):
    self.friend = friendProgram

  def addMessage(self, val):
    self.message_queue.append(val)

  def execInstruction(self):
    if self.instruction_index < 0 or self.instruction_index >= len(self.in_l):
      print "Program", self.id, "Terminated"
      self.waiting = True
      return
  
    command = self.in_l[self.instruction_index]
    cmd = command.split()
    op = cmd[0]
    if self.instruction_index == 11:
      print "Reached index 11"
      print self.registers
      sys.exit()
    print "Instruction index", self.instruction_index, "command", cmd
    if op == 'set':
      x = cmd[1]
      y = cmd[2]
      if y in self.registers_l:
        self.registers[x] = self.registers[y]
      else:
        self.registers[x] = int(y)

    elif op == 'sub':
      x = cmd[1]
      y = cmd[2]
      if y in self.registers_l:
        self.registers[x] -= self.registers[y]
      else:
        self.registers[x] -= int(y)

    elif op == 'mul':
      self.mult_count += 1
      x = cmd[1]
      y = cmd[2]
      if y in self.registers_l:
        self.registers[x] *= self.registers[y]
      else:
        self.registers[x] *= int(y)
    
    elif op == 'jnz':
      x = cmd[1]
      y = cmd[2]
      if x in self.registers_l:
        x_val = self.registers[x]
      else:
        x_val = int(x)
      if y in self.registers_l:
        y_val = self.registers[y]
      else:
        y_val = int(y)
      if x_val != 0:
        self.instruction_index += y_val - 1
    else:
      assert(False)
    
    self.instruction_index += 1

def part1():
  in_l =  s.split('\n')
  registers_l = []
  for command in in_l:
    register = command.split()[1]
    if register >= 'a' and register <= 'z':
      registers_l.append(register)

  program0 = Program(0, registers_l, in_l)
  while program0.isNotWaiting():
    program0.execInstruction()

  print "Program mult count", program0.mult_count

def part2():
  in_l =  s.split('\n')
  for ind, cmd in enumerate(in_l):
    print "Instruction", ind, cmd
  registers_l = []
  for command in in_l:
    register = command.split()[1]
    if register >= 'a' and register <= 'z':
      registers_l.append(register)

  program0 = Program(0, registers_l, in_l)
  program0.setRegister('a', 1)
  while program0.isNotWaiting():
    program0.execInstruction()

  print "Program mult count", program0.mult_count

def checkIfPrimes():
  b = 109900
  c = 126900
  h = 0
  for b in range(109900, c + 1, 17):
      if not isPrime(b):
          h += 1
  
  print "h", h

def optimizedProgram():
  a = 1
  c = 126900 
  b = 109900 
  e = 2 
  d = 2 
  g = 0
  f = 1
  h = 0 
  p = 0
  while True:
    #Ins 8
    f = 1
    #Ins 9
    d = 2
    while True:
      #Ins 10
      e = 2
      while True:
        #Ins 11
        g = d
        #Ins 12
        g *=e
        #Ins 13
        g -= b
        #Ins 14
        if g == 0:
          #Ins 15
          f = 0
        #Ins 16
        e -= 1
        #Ins 17
        g = e
        #Ins 18
        g -= b
        #Ins 19
        if g == 0:
          break
      #Ins 20
      d -= 1
      #Ins 21
      g = d
      #Ins 22
      g -= b
      #Ins 23
      if g == 0:
        break
      #Ins 24
      if f == 0:
        #Ins 25
        h -= 1
      #Ins 26
      g = b
      #Ins 27
      g -= c
      #Ins 28
      if g == 0:
        #Ins 29 will terminate the program
        print "h", h
        sys.exit()
      #Ins 30
      b -= 17

#part1()
checkIfPrimes()
#optimizedProgram()
#part2()
