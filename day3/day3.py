#!/usr/bin/env python
import sys

def parseInput():
    file = open("input.txt")
    return file.readline()[:-1]  # Skip the \n at the end..


class Location():
  def __init__(self, lap, side, posInSide, sideLength):
    self.lap = lap
    self.side = side
    self.posInSide = posInSide
    self.sideLength = sideLength
  def display(self):
    print "Lap:", self.lap, "Side:", self.side, "posInSide:", self.posInSide, "sideLength:", self.sideLength

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
    locations.append(Location(lap, 0, locationInSide, sideLength))
    for loc in locations:
      loc.display()

def part2():
  sum = 0
  numLocations = 1
  lap = 2
  sideLength = 0
  myNum = int(parseInput())
  index = 0
  locations = []
  for lap in xrange(1, 10):
    sideLength = 2 * lap - 1 
    numLocations = 2 * sideLength + 2 * (sideLength - 2)
    for locInLap in xrange(numLocations):
       locationInSide = locInLap % (sideLength - 1)
       side = locInLap // (sideLength - 1)
       locations.append(Location(lap, side, locationInSide, sideLength))

  for loc in locations:
    loc.display()
  
part1()
part2()
