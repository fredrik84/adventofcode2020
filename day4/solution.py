#!/usr/bin/python3
import re
import pprint

expected_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]

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

c = 0
for row in data:
  if row:
    r = {}
    tmp = {x.split(':', 1)[0].strip(): x.split(':', 1)[1].strip() for x in row}
    if all(key in tmp for key in expected_fields):
      if 'cid' in tmp:
        del tmp['cid']
      v = int(tmp['byr'])
      if v < 1920 or v > 2002 or not len(str(v)) == 4: continue
      v = int(tmp['iyr'])
      if v < 2010 or v > 2020 or not len(str(v)) == 4: continue
      v = int(tmp['eyr'])
      if v < 2020 or v > 2030 or not len(str(v)) == 4: continue
      v = int(tmp['hgt'][:-2])
      k = str(tmp['hgt'][-2:])
      if k in ('cm', 'in'):
        if k == 'cm':
          if v > 193 or v < 150: continue
        elif k == 'in':
          if v > 76 or v < 59: continue
      else:
        continue

      if not re.match(r'^#[0-9a-f]{3}', tmp['hcl']): continue
      if not tmp['ecl'] in ('amb blu brn gry grn hzl oth'.split()):
        continue
      if not len(tmp['pid']) == 9:
        print(tmp['pid'])
        continue


      c += 1
print("{} valid passes of {} totally".format(c,len(data)))
