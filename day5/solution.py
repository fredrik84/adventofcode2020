#!/usr/bin/python3
with open('input.txt') as f:
  data = f.readlines()

seats = []
for p in data:
  try:
    p = p.strip()
    row = list(range(0,128))
    for k in p[:-3]:
      l = int(len(row)/2)
      if k == 'B':
        row = row[l:]
      elif k == 'F':
        row = row[:l]

    col = list(range(0,8))
    for k in p[-3:]:
      l = int(len(col)/2)
      if k == 'L':
        col = col[:l]
      elif k == 'R':
        col = col[l:]
    seat = row[0] * 8 + col[0]
    print(seat, p.strip())
    seats.append(seat)
  except Exception as msg:
    print(msg)
    exit()

s = list(sorted(seats))
d = [x for x in range(s[0], s[-1]+1) if x not in s]
print(d)
