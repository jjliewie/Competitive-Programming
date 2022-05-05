import sys

sys.stdin = open("mountains.in", "r")
sys.stdout = open("mountains.out", "w")

t = sys.stdin.readline

n = int(t())
use = []
for _ in range(n):
    a, b = map(int, t().split())
    use.append((a - b, a + b))

use.sort(key=lambda x: (x[0], -x[1]))
cur = use[0][1]

res = 1

for i in range(1, n):
    end = use[i][1]
    if end > cur:
        cur = end
        res += 1
print(res)