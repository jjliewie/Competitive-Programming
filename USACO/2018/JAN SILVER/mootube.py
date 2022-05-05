from collections import deque
import sys

t = sys.stdin.readline

a, b = map(int, t().split())

edge = [[] for _ in range(a+1)]

for _ in range(a-1):
    x, y, z = map(int, t().split())
    edge[x].append([y, z])
    edge[y].append([x, z])

def bfs(r, start):

    ans = 0

    visited = [False] * (a+1)

    q = deque()
    q.append(start)

    visited[start] = True

    while q:
        node = q.pop()
        for p, v in edge[node]:
            if not visited[p] and v >= r:
                q.appendleft(p)
                visited[p] = True
                ans += 1
    return ans

ans = []

for _ in range(b):
    c, d = map(int, t().split())
    cnt = bfs(c, d)
    ans.append(cnt)

for i in ans:
    print(i)