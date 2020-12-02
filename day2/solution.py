#!/usr/bin/python
import re
with open('input.txt') as f:
  d = list(map(str.strip, f.readlines()))

valid = []
for x in d:
  req, data = x.split(": ")
  length, key = req.split()
  l, t = length.split('-')
  if int(l) <= data.count(key) <= int(t):
    valid.append(data)

print("part 1:", len(valid))

valid = []
for x in d:
  req, data = x.split(": ")
  length, key = req.split()
  l, t = length.split('-')
  if data[int(l)-1] == key and data[int(t)-1] == key:
    continue
  elif not data[int(l)-1] == key and not data[int(t)-1] == key:
    continue
  elif data[int(l)-1] == key or data[int(t)-1] == key:
    valid.append(data)


print("part 2:", len(valid))
