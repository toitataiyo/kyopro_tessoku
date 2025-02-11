#! /usr/bin/env python

n, k = map(int, input().split())
n_yakusu = [i for i in range(1, n+1)]
ans = 0
for a in n_yakusu:
    for b in n_yakusu:
        c = k-a-b
        if c > 0 and c <= n:
            ans += 1
        
print(ans)