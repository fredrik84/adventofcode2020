#!/usr/bin/python3
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--steps', nargs='+', default=["3:1"], help='3:1 is 3 steps right, 1 down')
parser.add_argument('--start-step', default=0, type=int, help='Starting step')
parser.add_argument('--summary', action='store_true', default=False)
args = parser.parse_args()

with open('input.txt') as f:
  d = list(map(str.strip, f.readlines()))


summary = {}
for arg in args.steps:
  rstep, dstep = list(map(int, arg.split(':')))
  step = args.start_step
  result = {}
  for y, c in enumerate(d):
    if not y % dstep == 0:
      continue
    k = step % len(c)
    v = c[k]
    step += rstep
    if v not in result:
      result[v] = 0
    result[v] += 1
  summary[arg] = result['#']

if args.summary:
  sres = 1
  for k, s in summary.items():
    sres *= s
  print(sres)
else:
  print(summary)
