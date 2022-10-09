import sys
t = sys.stdin.readline

n, q = map(int, t().split())
forest = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for idx, c in enumerate(t().strip()):
        tree = c == '*'
        tmp = forest[i-1][idx+1] + forest[i][idx] - forest[i-1][idx] + tree
        forest[i][idx + 1] += tmp

def solve(a, b, c, d, graph):
    return graph[c][d] - graph[a-1][d] - graph[c][b-1] + graph[a-1][b-1]

res = []
for _ in range(q):
    y1, x1, y2, x2 = map(int, t().split())
    res += [solve(y1, x1, y2, x2, forest)]

for ans in res:
    print(ans)