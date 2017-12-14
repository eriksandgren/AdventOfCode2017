#!/usr/bin/env python
from collections import deque

s = """jzgqcdpd"""
class Square():
  def __init__(self, val):
    self.val = int(val)
    self.visited = False
    self.group = None


def search(grid_mat, y, x):
  directions = [(0,1), (1,0), (-1,0), (0,-1)]

  grid_mat[y][x].visited = True
  for (dx, dy) in directions:
    if (y + dy >= 0) and (y + dy < 128) and (x + dx >= 0) and (x + dx <
128):
      if not grid_mat[y + dy][x + dx].visited and grid_mat[y + dy][x +
dx].val == 1:
        search(grid_mat, y + dy, x + dx)

def knotHash(string):
  ascii_l = [ord(x) for x in string]
  input_l = ascii_l + [17, 31, 73, 47, 23]
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
  strHex = ""
  for x in hash_l:
    strHex += "%0.2x" % x

  scale = 16 ## equals to hexadecimal
  num_of_bits = 128
  binary_data = bin(int(strHex, scale))[2:].zfill(num_of_bits)
  return binary_data

grid = []
numUsed = 0
for line in xrange(128):
  string = s + '-' + str(line)
  bin_data = knotHash(string)
  numUsed += bin_data.count('1')
  grid += [bin_data]

print "Number of used squares", numUsed

grid_mat = []
for line in grid:
  line_mat = []
  for sq in line:
    line_mat.append(Square(sq))
  grid_mat.append(line_mat)

numRegions = 0
for y in xrange(128):
  for x in xrange(128):
    if not grid_mat[y][x].visited and grid_mat[y][x].val == 1:
      numRegions += 1
      search(grid_mat, y, x)

print "Number of regions", numRegions

