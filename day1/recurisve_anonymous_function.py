#!/usr/bin/python3
fu = (lambda f:[(lambda a: [a*i for i in f if a+i == 2020])(a) for a in f])
print(list(filter(None, fu(list(map(int, open('input.txt').readlines()))))).pop()[0])
