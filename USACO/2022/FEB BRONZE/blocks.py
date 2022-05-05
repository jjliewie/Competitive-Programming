import sys
from collections import Counter

t = sys.stdin.readline

n = int(t())

blocks = []

for _ in range(4):
    blocks.append(set(t()))

def sol():
    x = t().strip()
    k = Counter(x)

    for a in blocks[0]:
        for b in blocks[1]:
            for c in blocks[2]:
                for d in blocks[3]:

                    possible = Counter([a, b, c, d])

                    for i in k:
                        if possible[i] < k[i]:
                            break
                    else:
                        print("YES")
                        return
    print("NO")
    return

for _ in range(n):
    sol()
