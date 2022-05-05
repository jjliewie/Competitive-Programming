import sys
from collections import deque

t = sys.stdin.readline

a = int(t())
b = []
for _ in range(a):
    x, y, z = map(int, t().split())
    b.append([x, y, z])

def bfs(x, y, limit):
    
    ans = 0
    visited = []

    q = deque()
    q.append((x, y, limit))
    visited.append((x, y, limit))

    while q:
        node = q.pop()
        x_coor = node[0]
        y_coor = node[1]

        for i in b:
            x_ncoor = i[0]
            y_ncoor = i[1]

            dist = ((x_coor-x_ncoor)**2) + ((y_coor-y_ncoor)**2)
        q.append(dist)

    return ans

max_reach = 0

for i in b:
    reach = bfs(i[0], i[1], i[2])
    max_reach = max(reach, max_reach)

print(max_reach)