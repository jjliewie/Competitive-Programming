import sys
from collections import deque
t = sys.stdin.readline

b_time, e_time = set(), set()

path = dict()
n, m = map(int, t().split())
for i in range(n):
    path[i] = []
for _ in range(m):
    l1, l2, s1, s2 = map(int, t().split())
    path[l1].append([l2, s1, s2])

def bfs(time, j):
    q = deque()
    q.append([1, 0])
    while q:
        node = q.pop()
        if node[0] == n:
            time.add(node[1])
        else:
            for tmp in path[node[0]]:
                q.appendleft([tmp[0], node[1]+tmp[j]])

bfs(b_time, 1)
bfs(e_time, 2)

minimum = 16000

for i in b_time:
    for j in e_time:
        if i == j:
            minimum = min(i, minimum)

if minimum == 16000:
    print("IMPOSSIBLE")
else:
    print(minimum)