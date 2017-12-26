#!/usr/bin/env python
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
s = """
......#.#....####.##.#...
##.##.#.####.##.#.#.##..#
.#.#######.#..###......#.
#####..###.##..####.#..##
.#..#.##...#.####.#....#.
#.#...#.#####.#.#####..##
..##.#..######....####.##
#.##.#....#.#.##........#
.#....#....###.#....####.
....#..##.#.#.##.#....#.#
.#.##.#.####..#..#.##..##
##.####.#..###...#.#...##
....#....#..#..####.##...
..#.#.#.#..#.###...#...##
.#..#..##..##.#.#..##.#..
####.#.#...##.#..##.###..
###.#....#...#..#..#...##
.##....##.......####.#.##
#.#.##.#.#..#.#..##..####
...#..##.#.####.....##.##
.#.##.#####.#.#....#####.
##......#..#.###..####.##
..#...#########.....#..##
##..###.##...###.#.#.#.#.
..###.###.##.#.###....#.#
""".strip()

# s = """
# ..#
# #..
# ...
# """.strip()

def printMat(grid_l, x = -1, y = -1):
  if x == -1 and y == -y:
    for line in grid_l:
      print ''.join(line)
  else:
    for ind, line in enumerate(grid_l):
      printLine = ' '.join(line)
      if ind == y:
        print (printLine[:x * 2 - 1] + bcolors.OKGREEN  + '[' + printLine[x * 2] + ']' + bcolors.ENDC + printLine[x * 2 + 2 :])
      else:
        print printLine

def part1():
  in_l = s.split('\n')
  print len(in_l)
  for l in in_l:
    print l, len(l)
  grid_size = 499
  sides_size = (grid_size - len(in_l)) / 2
  grid = []
  for row in xrange(grid_size):
    if row in range(sides_size, sides_size + len(in_l)):
      grid.append("." * sides_size + in_l[row - sides_size] + "." * sides_size)
    else:
      grid.append("." * grid_size)

  grid_l = []
  for line in grid:
    grid_l.append(list(line))

  x = grid_size / 2
  y = grid_size / 2
  dx = 0
  dy = -1
  numInfections = 0
  for step in xrange(10000):
    #printMat(grid_l, x, y)
    #print

    if grid_l[y][x] == '#':
      # Turn right
      if dx == 0:
        dx = -dy
        dy = 0
      else:
        dy = dx
        dx = 0
      grid_l[y][x] = '.'
    elif grid_l[y][x] == '.':
      if dx == 0:
        dx = dy
        dy = 0
      else:
        dy = -dx
        dx = 0
      grid_l[y][x] = '#'
      numInfections += 1
    y += dy
    x += dx

  print "Number of infections", numInfections


def part2():
  in_l = s.split('\n')
  print len(in_l)
  for l in in_l:
    print l, len(l)
  grid_size = 499
  sides_size = (grid_size - len(in_l)) / 2
  grid = []
  for row in xrange(grid_size):
    if row in range(sides_size, sides_size + len(in_l)):
      grid.append("." * sides_size + in_l[row - sides_size] + "." * sides_size)
    else:
      grid.append("." * grid_size)

  grid_l = []
  for line in grid:
    grid_l.append(list(line))

  x = grid_size / 2
  y = grid_size / 2
  dx = 0
  dy = -1
  numInfections = 0
  for step in xrange(10000000):
    #printMat(grid_l, x, y)
    #print

    #Clean
    if grid_l[y][x] == '.':
      # Turn left
      if dx == 0:
        dx = dy
        dy = 0
      else:
        dy = -dx
        dx = 0
      grid_l[y][x] = 'W'
    # Weakened
    elif grid_l[y][x] == 'W':
      # No turn
      grid_l[y][x] = '#'
      numInfections += 1
    # Infected
    elif grid_l[y][x] == '#':
      # Turn right
      if dx == 0:
        dx = -dy
        dy = 0
      else:
        dy = dx
        dx = 0
      grid_l[y][x] = 'F'
    # Flagged
    elif grid_l[y][x] == 'F':
      # Reverse direction
      dy = -dy
      dx = -dx
      grid_l[y][x] = '.'
    y += dy
    x += dx

  print "Number of infections", numInfections
part2()