#!/usr/bin/env python
import sys

s = """ 
set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 826
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
""".strip()
def part1():
  registers = {}
  in_l =  s.split('\n')
  registers_l = []
  played_frequency = -1
  for command in in_l:
    register = command.split()[1]
    if register >= 'a' and register <= 'z':
      registers[register] = 0
      registers_l.append(register)

  print registers
  instruction_index = 0
  while instruction_index >= 0 and instruction_index < len(in_l):
    command = in_l[instruction_index]
    cmd = command.split()
    print cmd
    op = cmd[0]
    
    if op == 'snd':
      x = cmd[1]  
      if x in registers_l:
        freq = registers[x]
      else:
        freq = int(x)
      played_frequency = freq
      print "Sounds", freq
    elif op == 'set':
      x = cmd[1]
      y = cmd[2]
      if y in registers_l:
        registers[x] = registers[y]
      else:
        registers[x] = int(y)
      print "Setting"
    elif op == 'add':
      x = cmd[1]
      y = cmd[2]
      if y in registers_l:
        registers[x] += registers[y]
      else:
        registers[x] += int(y)
      print "Adding"

    elif op == 'mul':
      x = cmd[1]
      y = cmd[2]
      if y in registers_l:
        registers[x] *= registers[y]
      else:
        registers[x] *= int(y)
      print "Multiplying"
    
    elif op == 'mod':
      x = cmd[1]
      y = cmd[2]
      if y in registers_l:
        registers[x] %= registers[y]
      else:
        registers[x] %= int(y)
      print "Modulus"
    elif op == 'rcv':
      x = cmd[1]
      if x in registers_l:
        val = registers[x]
      else:
        val = int(x)

      if val != 0:
        print "Recovers", played_frequency
        sys.exit()

    elif op == 'jgz':
      x = cmd[1]
      y = cmd[2]
      if x in registers_l:
        x_val = registers[x]
      else:
        x_val = int(x)
      if y in registers_l:
        y_val = registers[y]
      else:
        y_val = int(y)
      if x_val > 0:
        instruction_index += y_val - 1
        print "Jumps"
    else:
      assert(False)
    
    instruction_index += 1

class Program():
  def __init__(self, programId, registers_l, in_l):
    self.id = programId
    self.send_count = 0
    self.recv_count = 0
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
    print "Program", self.id, cmd

    op = cmd[0]
    if op == 'snd':
      x = cmd[1]
      if x in self.registers_l:
        x_val = self.registers[x]
      else:
        x_val = int(x)
      self.send_count += 1
      self.friend.addMessage(x_val)

    elif op == 'set':
      x = cmd[1]
      y = cmd[2]
      if y in self.registers_l:
        self.registers[x] = self.registers[y]
      else:
        self.registers[x] = int(y)
    elif op == 'add':
      x = cmd[1]
      y = cmd[2]
      if y in self.registers_l:
        self.registers[x] += self.registers[y]
      else:
        self.registers[x] += int(y)

    elif op == 'mul':
      x = cmd[1]
      y = cmd[2]
      if y in self.registers_l:
        self.registers[x] *= self.registers[y]
      else:
        self.registers[x] *= int(y)
    
    elif op == 'mod':
      x = cmd[1]
      y = cmd[2]
      if y in self.registers_l:
        self.registers[x] %= self.registers[y]
      else:
        self.registers[x] %= int(y)
    elif op == 'rcv':
      x = cmd[1]
      if self.message_queue:
        self.waiting = False
        val = self.message_queue.pop(0)
        if x in self.registers_l:
          self.registers[x] = val
        else:
          assert(False)
      else:
        self.waiting = True
        return
        

    elif op == 'jgz':
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
      if x_val > 0:
        self.instruction_index += y_val - 1
    else:
      assert(False)
    
    self.instruction_index += 1

def part2():
  in_l =  s.split('\n')
  registers_l = []
  for command in in_l:
    register = command.split()[1]
    if register >= 'a' and register <= 'z':
      registers_l.append(register)

  program0 = Program(0, registers_l, in_l)
  program1 = Program(1, registers_l, in_l)
  program0.setFriend(program1)
  program1.setFriend(program0)
  while program0.isNotWaiting() or program1.isNotWaiting():
    program0.execInstruction()
    program1.execInstruction()

  print "Program 1 send count", program1.send_count

    
  
#part1()
part2()
