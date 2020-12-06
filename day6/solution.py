#!/usr/bin/python3
import re

data = [[]]
index = 0
with open('input.txt') as f:
  d = f.readlines()
  for r in d:
    if re.match(r'^\n', r):
      index += 1
      data.append([])
      continue
    for r2 in r.split():
      data[index].append(r2)

total = 0
for g in data:
  c = list(set("".join(g)))
  if len(g) > 1:
    users = len(g)
    s = "".join(list(set([char for char in "".join(g)])))
    for char in s:
      l = len([c1 for c1 in "".join(g) if char == c1])
      if l == users:
        v = 1
      else:
        v = 0
      total += v
  else:
    v = len(g[0])
    total += v

  #print(cl, users, c, g, total)

print(total)
