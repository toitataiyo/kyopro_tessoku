#! /usr/bin/env python
import itertools

N, Q = map(int, input().split())
nyujousya = map(int, input().split())
# itertools.accumulateで累積和になる
accum_nyujousya = [i for i in itertools.accumulate(nyujousya)]
accum_nyujousya.insert(0, 0)
for _ in range(Q):
    l, r = map(int, input().split())
    raijousya = accum_nyujousya[r] - accum_nyujousya[l-1]
    print(raijousya)