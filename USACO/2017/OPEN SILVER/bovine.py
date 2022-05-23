# partial, but I genuinely believe this is the best possible solution

from itertools import combinations

with open('cownomics.in') as r:
    input = r.readline
    n, m = map(int, input().split())
    s = [input().strip() for _ in range(n)]
    p = [input().strip() for _ in range(n)]

pos = 0
acgt = set()

for a, b, c in combinations(range(m), 3):
    acgt.clear()
    for i in s: 
        acgt.add(sum(i[a], i[b], i[c]))
    for i in p: 
        if sum(i[a], i[b], i[c]) in acgt: break
    else:
        pos += 1

print(pos, file=open('cownomics.out', 'w'))