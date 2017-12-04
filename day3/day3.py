#!/usr/bin/env python
import sys

def parseInput():
    file = open("input.txt")
    return file.readline()[:-1]  # Skip the \n at the end..


class Location():
<<<<<<< HEAD
  def __init__(self, lap, side, posInSide, sideLength, index):
=======
  def __init__(self, lap, side, posInSide, sideLength):
>>>>>>> c104d29347d5b89ea86175425c7bb9a257457b14
    self.lap = lap
    self.side = side
    self.posInSide = posInSide
    self.sideLength = sideLength
<<<<<<< HEAD
    self.index = index
  def display(self):
    print "Lap:", self.lap, "Side:", self.side, "posInSide:", self.posInSide, "sideLength:", self.sideLength, "index", self.index
=======
  def display(self):
    print "Lap:", self.lap, "Side:", self.side, "posInSide:", self.posInSide, "sideLength:", self.sideLength
>>>>>>> c104d29347d5b89ea86175425c7bb9a257457b14

def part1():
    myLoc = int(parseInput())
    numLocations = 1
    lap = 2
    sideLength = 0
    locations = []
    while numLocations < myLoc:
      sideLength = 2 * lap - 1 
      numLocations += 2 * sideLength + 2 * (sideLength - 2)
      print "Lap: ", lap, " numLocations: ", numLocations
      lap += 1
    numLocations -= 2 * sideLength + 2 * (sideLength - 2)
    lap -= 1
    print "lap", lap
    print "numLocations ", numLocations    
    print "sideLength ", sideLength
    print "locationsIntoThisLap", myLoc -numLocations
    locationsIntoThisLap = myLoc -numLocations
    print "locationInSide", (myLoc -numLocations) % (sideLength - 1)
    locationInSide = locationsIntoThisLap % (sideLength - 1)
    print "distance to side-middle", abs(locationInSide - (sideLength // 2))
    distanceFromSideMiddle = abs(locationInSide - (sideLength // 2))
    distanceTo1 = lap - 1
    totalDistance = distanceFromSideMiddle + distanceTo1
    print "Total distance", totalDistance


def part2():
  sum = 0
  numLocations = 1
  lap = 2
  sideLength = 0
  myNum = int(parseInput())

  locations = []
  locations.append(Location(1, 0, 0, 0, 1))
  index = 1

  index = 0
  locations = []
  for lap in xrange(1, 10):
    sideLength = 2 * lap - 1 
    numLocations = 2 * sideLength + 2 * (sideLength - 2)
    for locInLap in xrange(numLocations):

       index += 1
       locationInSide = locInLap % (sideLength - 1)
       side = locInLap // (sideLength - 1)
       locations.append(Location(lap, side, locationInSide, sideLength, index))

  sums = [1, 1, 2, 4, 5, 10, 11, 23, 25]
  startInd = len(sums) - 1

  for ind in xrange(len(sums), len(locations)):
    loc = locations[ind]
    inds = []
    if loc.posInSide == 0 and loc.side == 0:
      ind1 = ind - 1
      ind2 = ind - (loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3))
      ind3 = ind2 + 1
      inds = [ind1, ind2, ind3] 
      # print "ind", ind
      # print "ind1", ind1
      # print "ind2", ind2
      # print "ind3", ind3
      # print "side", loc.side
      # print "posInSide", loc.posInSide
      # print "spec"
      
    elif loc.posInSide == 0:
      ind1 = ind - 1
      ind2 = ind - (loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3))
      inds = [ind1, ind2]
      # print "ind", ind
      # print "ind1", ind1
      # print "ind2", ind2
      # print "side", loc.side
      # print "posInSide", loc.posInSide

    elif loc.posInSide == 1 and loc.side == 0:
        ind1 = ind - 1
        ind2 = ind - (loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3))
        inds = [ind1, ind2]
        # print "ind", ind
        # print "ind1", ind1
        # print "ind2", ind2
        # print "side", loc.side
        # print "posInSide", loc.posInSide

    elif loc.posInSide == 1:
      ind1 = ind - 1
      ind2 = ind - 2
      ind3 = ind - (1 + loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3)) 
      ind4 = ind3 + 1
      inds = [ind1, ind2, ind3, ind4]
      # print "ind", ind
      # print "ind1", ind1
      # print "ind2", ind2
      # print "ind3", ind3
      # print "ind4", ind4
      # print "side", loc.side
      # print "posInSide", loc.posInSide

    elif (loc.posInSide == loc.sideLength - 2) and loc.side == 3:
      ind1 = ind - 1
      ind2 = ind - (1 + loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3))
      ind3 = ind - (2 + loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3)) 
      ind4 = ind2 + 1
      inds = [ind1, ind2, ind3, ind4]
      # print "ind", ind
      # print "ind1", ind1
      # print "ind2", ind2
      # print "ind3", ind3
      # print "ind4", ind4
      # print "side", loc.side
      # print "posInSide", loc.posInSide
      # print "pos sideLength - 2"

    elif loc.posInSide == loc.sideLength - 2:
      ind1 = ind - 1
      ind2 = ind - (1 + loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3))
      ind3 = ind - (2 + loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3)) 
      inds = [ind1, ind2, ind3]
      # print "ind", ind
      # print "ind1", ind1
      # print "ind2", ind2
      # print "ind3", ind3
      # print "side", loc.side
      # print "posInSide", loc.posInSide
      # print "pos sideLength - 2"

    elif loc.side == 0 and loc.posInSide == 2:
      ind1 = ind - 1
      ind2 = ind  - (loc.posInSide + loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3)) + loc.posInSide - 2
      ind3 = ind2 + 1
      ind4 = ind3 + 1
      ind2 = ind - 2
      inds = [ind1, ind2, ind3, ind4]
      # print "ind", ind
      # print "ind1", ind1
      # print "ind2", ind2
      # print "ind3", ind3
      # print "ind4", ind4
      # print "side", loc.side
      # print "posInSide", loc.posInSide
      # print "pos in the middle"

    else:
      ind1 = ind - 1
      ind2 = ind  - (loc.posInSide + loc.side * (loc.sideLength - 1) + (4 - loc.side) * (loc.sideLength - 3)) + loc.posInSide - 2
      ind3 = ind2 + 1
      ind4 = ind3 + 1
      inds = [ind1, ind2, ind3, ind4]
      # print "ind", ind
      # print "ind1", ind1
      # print "ind2", ind2
      # print "ind3", ind3
      # print "ind4", ind4
      # print "side", loc.side
      # print "posInSide", loc.posInSide
      # print "pos in the middle"
      
    sum = 0
    for ind in inds:
      sum += sums[ind - 1]
    sums.append(sum)
    # print inds
    print

  for i in xrange(51):
    print sums[i]
part1()
part2()

'''
37  36  35  34  33  32  31  
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28
41  20   7   8   9  10  27
42  21  22  23  24  25  26
43  44  45  46  47  48  49 50
'''
=======
       locationInSide = locInLap % (sideLength - 1)
       side = locInLap // (sideLength - 1)
       locations.append(Location(lap, side, locationInSide, sideLength))

  for loc in locations:
    loc.display()
  
part1()
part2()
>>>>>>> c104d29347d5b89ea86175425c7bb9a257457b14
