# partial, but I genuinely believe this is the best possible solution

from itertools import combinations

with open('cownomics.in') as r:
    input = r.readline
    n, m = map(int, input().split())
    spotty_cows = [input().strip() for _ in range(n)]
    plain_cows = [input().strip() for _ in range(n)]

pos = 0
acgt = set()

for a, b, c in combinations(range(m), 3):
    acgt.clear()
    for genomes in spotty_cows: 
        acgt.add(genomes[a] + genomes[b] + genomes[c])
    for genomes in plain_cows: 
        if genomes[a] + genomes[b] + genomes[c] in acgt: 
            break
    else:
        pos += 1

print(pos, file=open('cownomics.out', 'w'))