#!/usr/bin/python3
import pprint
import re

data = {}
with open('example.txt') as f:
  for r in f.readlines():
    t, c = r.strip().replace(".", "").split(' contain ')
    t = re.sub(r'bags*$', '', t).strip()
    if t not in data:
      data[t] = {}
    for constraints in c.split(", "):
      v, ct = constraints.split(" ", 1)
      ct = re.sub(r'bags*$', '', ct).strip()
      if v == 'no':
        continue
      v = int(v)
      if ct not in data[t]:
        data[t][ct] = 0
      data[t][ct] += v

search = 'shiny gold'
out = []
total = 0
for t, c in data.items():
  if search not in c:
    continue
  total += c[search]
  out.append({t:c})

pprint.pprint(total)
