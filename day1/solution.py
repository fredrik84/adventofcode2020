#!/usr/bin/python3
print("part 1:", list(map(lambda f: [x*y for x in f for y in f if x+y==2020].pop(), [list(map(int, open('input.txt').read().split()))])).pop())
print("part 2:", list(map(lambda f: [x*y*z for x in f for y in f for z in f if x+y+z==2020].pop(), [list(map(int, open('input.txt').read().split()))])).pop())
