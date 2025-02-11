#! /usr/bin/env python

n = int(input())
amari_list = []

for i in range(10):
    if n != 0:
        amari = n % 2
        amari_list.append(str(amari))
        n = n//2
    else:
        amari_list.append(str(0))

amari_list.reverse()
result = "".join(amari_list)
print(result)