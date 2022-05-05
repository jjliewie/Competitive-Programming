import sys
from collections import deque

sys.stdin = open("mooyomooyo.in", "r")
sys.stdout = open("mooyomooyo.out", "w")

input = sys.stdin.readline

# possible directions to visit all connected regions
directions = [
    (1, 0), 
    (0, 1), 
    (-1, 0), 
    (0, -1)
]

a, b = map(int, input().split())

def gravity(graph, s, coors):

    for i in range(s // 2):
        for j in range(5):
            graph[i][j], graph[j][i] = graph[j][i], graph[i][j]
    
    for y, x in coors:
        graph[y].pop(x)
        graph[y].append(0)
    
    for i in range(5):
        for j in range(s // 2):
            graph[i][j], graph[j][i] = graph[j][i], graph[i][j]
    
    return graph

# bfs to mark all connected regions
def bfs(x, y, graph, visited):
        q = deque()
        q.append((x, y))
        visited[y][x] = True
        coors = [(x, y)]
        while q:
            x, y = q.pop()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # boundaries
                if 0 <= nx < 10 and 0 <= ny < a:

                    # check if already visited
                    if graph[ny][nx] == graph[y][x] and not visited[ny][nx]:
                        q.appendleft((nx, ny))
                        visited[ny][nx] = True
                        coors.append((nx, ny))
        return coors

def mooyo(graph):

    visited = [[False] * 10 for _ in range(a)]
    all_coors = []

    for i in range(a):
        for j in range(10):
            # check if visited
            if graph[i][j] != 0 and not visited[i][j]:
                temp = bfs(j, i, graph, visited)
                if len(temp) >= b:
                    all_coors += temp

    if not all_coors:
        return graph

    for x, y in all_coors:
        graph[y][x] = 0
    
    for x in range(10):
        blocks = []
        for y in range(a):
            if graph[y][x] != 0:
                blocks.append(graph[y][x])
                graph[y][x] = 0

        y = a - 1
        while blocks:
            node = blocks.pop()
            graph[y][x] = node
            y -= 1
    
    return mooyo(graph)
    

c = []
for i in range(a):
    tmp = list(map(int, list(input().strip())))
    c.append(tmp)

k = mooyo(c)
for i in k:
    i = [str(x) for x in i]
    print("".join(i))