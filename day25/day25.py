#!/usr/bin/env python
import sys

s = """
Begin in state A.
Perform a diagnostic checksum after 12208951 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state E.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state A.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state F.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
""".strip()

state = 'A'
steps = 12208951

tape = [0] * int(12208951 / 10)
index = int(len(tape) / 2)

for step in xrange(steps):
  if state == 'A':
    if tape[index] == 0:
      tape[index] = 1
      index += 1
      state = 'B'
    else:
      tape[index] = 0
      index -= 1
      state = 'E'
  elif state == 'B':
    if tape[index] == 0:
      tape[index] = 1
      index -= 1
      state = 'C'
    else:
      tape[index] = 0
      index += 1
      state = 'A'
  elif state == 'C':
    if tape[index] == 0:
      tape[index] = 1
      index -= 1
      state = 'D'
    else:
      tape[index] = 0
      index += 1
      state = 'C'
  elif state == 'D':
    if tape[index] == 0:
      tape[index] = 1
      index -= 1
      state = 'E'
    else:
      tape[index] = 0
      index -= 1
      state = 'F'
  elif state == 'E':
    if tape[index] == 0:
      tape[index] = 1
      index -= 1
      state = 'A'
    else:
      tape[index] = 1
      index -= 1
      state = 'C'
  elif state == 'F':
    if tape[index] == 0:
      tape[index] = 1
      index -= 1
      state = 'E'
    else:
      tape[index] = 1
      index += 1
      state = 'A'


print "Checksum", sum(tape)