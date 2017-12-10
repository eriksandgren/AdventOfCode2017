#!/usr/bin/env python

s = """206,63,255,131,65,80,238,157,254,24,133,2,16,0,1,3"""
add_seq = """17, 31, 73, 47, 23"""

def part1():
  input_l =  [int(x) for x in s.split(',')]
  ascii_l = [ord(x) for x in s]
  add_l = [int(x) for x in add_seq.split(',')]
  list_len = 256
  circ_list = range(list_len)
  skip_size = 0
  current_position = 0
  for length in input_l:
    if length > list_len:
      continue

    start = current_position
    end = current_position + length
    if end < list_len:
      circ_list[start : end] = circ_list[start : end][::-1]
    else:
      end = end % list_len
      list_slice = circ_list[start:] + circ_list[: end]
      list_slice = list_slice[::-1]
      circ_list[start:] = list_slice[: length - end]
      circ_list[:end] = list_slice[-end:]

    current_position = (current_position + length + skip_size) % list_len
    skip_size += 1
  print "Part 1", circ_list[0] * circ_list[1]


def part2():
  ascii_l = [ord(x) for x in s]
  add_l = [int(x) for x in add_seq.split(',')]
  input_l =  ascii_l + add_l
  list_len = 256
  circ_list = range(list_len)
  skip_size = 0
  current_position = 0
  rounds = 64
  for r in xrange(rounds):
    for length in input_l:
      start = current_position
      end = current_position + length

      if end <= list_len:
        circ_list[start : end] = circ_list[start : end][::-1]
      else:
        end = end % list_len
        list_slice = circ_list[start:] + circ_list[: end]
        list_slice = list_slice[::-1]
        circ_list[start:] = list_slice[: length - end]
        circ_list[:end] = list_slice[-end:]

      current_position = (current_position + length + skip_size) % list_len
      skip_size = (skip_size + 1) % list_len
  hash_l = []

  for part in xrange(list_len / 16):
    part_l = circ_list[part * 16 : part * 16 + 16]
    hash_val = 0
    for x in part_l:
      hash_val ^= x
    hash_l.append(hash_val)
 #   print len(part_l), part_l
  #print hash_l
  strHex = ""
  for x in hash_l:
    strHex += "%0.2x" % x
  print "Part 2", len(strHex), strHex
part1()
part2()
