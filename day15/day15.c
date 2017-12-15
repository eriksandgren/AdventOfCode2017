#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

uint64_t aFactor = 16807;
uint64_t bFactor = 48271;
uint64_t aStart = 699;
uint64_t bStart = 124;

void part1()
{
  uint64_t wantedElem = 40 * 1000000;
  uint64_t compared = 0;
  uint64_t matches = 0;

  uint64_t a = aStart;
  uint64_t b = bStart;
  while (compared < wantedElem)
  {
    a *= aFactor;
    a = a % 2147483647;

    b *= bFactor;
    b = b % 2147483647;  

    uint64_t tempA = a & 65535;
    uint64_t tempB = b & 65535;
    
    if (tempA == tempB)
    {
      matches++;
    }
    compared++;
  }
  printf("Part 1 matches = %lu\n", matches);
}

void part2()
{
  uint64_t wantedElem = 5 * 1000000;  
  uint64_t compared = 0;
  uint64_t matches = 0;
  bool foundA = false;
  bool foundB = false;
  
  uint64_t a = aStart;
  uint64_t b = bStart;

  while (compared < wantedElem)
  {
    if (foundA && foundB)
    {
      compared++;
      uint64_t tempA = a & 65535;
      uint64_t tempB = b & 65535;
      if (tempA == tempB)
      {
        matches++;
      }
      foundA = false;
      foundB = false;
    } 
    if (!foundA)
    {
      a *= aFactor;
      a = a % 2147483647;
      foundA = (a % 4) == 0;
    }
    if (!foundB)
    {
      b *= bFactor;
      b = b % 2147483647;  
      foundB = (b % 8) == 0;
    }
  }
  printf("Part 2 matches = %lu\n", matches);
}


void main()
{
  part1();
  part2();
}

