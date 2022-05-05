import sys
from collections import deque

sys.stdin = open("perimeter.in", "r")
sys.stdout = open("perimeter.out", "w")

t = sys.stdin.readline

n = int(t())
ice = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    ice.append(list(t()))

max_area = 0
min_peri = float('inf')

# check if out of bounds
def out(a, b, l):
    if a < 0 or b < 0 or a >= l or b >= l:
        return True
    return False

# bfs
def bfs(x, y):
    area, peri = 1, 0

    # possible directions
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.pop()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if out(nx, ny, n) or ice[nx][ny] == ".":
                peri += 1
            else:
                # check if already visited 
                if not visited[nx][ny]:
                    area += 1
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
    return area, peri

for i in range(n):
    for j in range(n):
        if ice[i][j] == "#" and not visited[i][j]:
            area, peri = bfs(i, j)

            if area > max_area:
                max_area, min_peri = area, peri
            elif area == max_area:
                if min_peri > peri:
                    max_area, min_peri = area, peri

print(max_area, min_peri)
