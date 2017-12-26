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
25/13
4/43
42/42
39/40
17/18
30/7
12/12
32/28
9/28
1/1
16/7
47/43
34/16
39/36
6/4
3/2
10/49
46/50
18/25
2/23
3/21
5/24
46/26
50/19
26/41
1/50
47/41
39/50
12/14
11/19
28/2
38/47
5/5
38/34
39/39
17/34
42/16
32/23
13/21
28/6
6/20
1/30
44/21
11/28
14/17
33/33
17/43
31/13
11/21
31/39
0/9
13/50
10/14
16/10
3/24
7/0
50/50
""".strip()

# s = """
# 0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10
# """.strip()

class Component():
  def __init__(self, line):
    tmp = line.split('/')
    self.ports = [int(x) for x in tmp]
    self.line = line
    self.connected_edge = None

  def hasPort(self, port):
    return port in self.ports
  
  def score(self):
    return sum(self.ports)

  def returnOtherPort(self, port):
    if self.ports[0] == int(port):
      return self.ports[1]
    else:
      return self.ports[0]

  def display(self):
    print self.line

def findConnections(components_l, port, built_list, score_list):
  for ind, comp in enumerate(components_l):
    if comp.hasPort(port):
      built_l = list(built_list)
      unused_components_l = list(components_l)
      built_l.append(comp)
      del unused_components_l[ind]
      findConnections(unused_components_l, comp.returnOtherPort(port), built_l, score_list)
  score = 0
  length = len(built_list)
  for comp in built_list:
    score += comp.score()
  score_list.append((score, length))

in_l = s.split('\n')
components_l = []
for line in in_l:
  components_l.append(Component(line))

unused_components_l = list(components_l)
built_list = []
score_list = []
findConnections(unused_components_l, 0, built_list, score_list)

longest_length = 0
longest_score = 0
strongest = 0
for score in score_list:
 if score[0] > strongest:
   strongest = score[0]

 if score[1] == longest_length and score[0] > longest_score:
   longest_length = score[1]
   longest_score = score[0]

 elif score[1] > longest_length:
   longest_length = score[1]
   longest_score = score[0]

print "Longest length", longest_length, "longest score", longest_score, "strongest score", strongest