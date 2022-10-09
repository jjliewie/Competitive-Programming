import sys
t = sys.stdin.readline

n, q = map(int, t().split())
forest = [[0]*(n) for _ in range(n)]

for i in range(n):
    for idx, c in enumerate(t().strip()):
        forest[i][idx] = (c == "*")

res = [0]*q

for i in range(q):
    y1, x1, y2, x2 = map(int, t().split())
    for r in range(y1-1, y2):
        for c in range(x1-1, x2):
            res[i] += forest[r][c]

for ans in res:
    print(ans)