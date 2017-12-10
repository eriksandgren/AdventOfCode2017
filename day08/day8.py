#!/usr/bin/env python

class Command():
  def __init__(self, string):
    split_string = string.split()
    self.split_string = split_string
    print split_string
    self.register = split_string[0]
    self.operation = split_string[1]
    self.val = int(split_string[2])
    self.comp_reg = split_string[4]
    self.condition = split_string[5]
    self.comp_val = int(split_string[6])

  def display(self):
    print self.split_string
    
def parseInput():
    with open ("input.txt", "r") as myfile:
        myInput = myfile.read()
    myInput = myInput.split('\n')
    return myInput

def printDict(myDict):
  for k, v in myDict.iteritems():
    print k, "Value", v
  print


def commandShouldBeExecuted(command, registers_dict):
  if command.condition == '==':
    return registers_dict[command.comp_reg] == command.comp_val
  elif command.condition == '!=':
    return registers_dict[command.comp_reg] != command.comp_val
  elif command.condition == '<':
    return registers_dict[command.comp_reg] < command.comp_val
  elif command.condition == '>':
    return registers_dict[command.comp_reg] > command.comp_val
  elif command.condition == '>=':
    return registers_dict[command.comp_reg] >= command.comp_val
  elif command.condition == '<=':
    return registers_dict[command.comp_reg] <= command.comp_val
  else:
    assert(False)

def executeCommand(command, registers_dict):
  if command.operation == 'inc':
    registers_dict[command.register] += command.val
  elif command.operation == 'dec':
    registers_dict[command.register] -= command.val
  else:
    assert(False)

def part1and2():
  input_l = parseInput()[:-1]

  registers_l = []
  commands_l = []
  for l in input_l:
    registers_l.append(l.split()[0])
    commands_l.append(Command(l))

  registers_set = set(registers_l)

  registers_dict = {}
  for reg in registers_set:
    registers_dict[reg] = 0
  maxValHeld = 0
  for c in commands_l:
    if commandShouldBeExecuted(c, registers_dict):
      print "Executing command"
      c.display()
      executeCommand(c, registers_dict)
    else:
      print "Not executing"
      c.display()
    if registers_dict[c.register] > maxValHeld:
      maxValHeld = registers_dict[c.register]

  values_l = []
  for k, v in registers_dict.iteritems():
    values_l.append(v)

  print "Current max val", max(values_l)
  print "Maximum value held", maxValHeld
part1and2()
