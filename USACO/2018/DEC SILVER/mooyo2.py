from collections import deque

# possible directions to visit all connected regions
DIRECTIONS = (
	(1, 0), 
	(0, 1), 
	(-1, 0), 
	(0, -1)
)

c = []
	
with open('mooyomooyo.in') as r:
	a, b = map(int, r.readline().split())
	for i in range(a):
		c.append(list(map(int, list(r.readline().strip()))))

mid = 5


def gravity(graph, s, coords):

	for i in range(s // 2):
		for j in range(mid):
			graph[i][j], graph[j][i] = graph[j][i], graph[i][j]
    
	for y, x in coords:
		graph[y].pop(x)
		graph[y].append(0)
    
	for i in range(mid):
		for j in range(s // 2):
			graph[i][j], graph[j][i] = graph[j][i], graph[i][j]
    
	return graph


# bfs to mark all connected regions
def mark_connected(x, y, graph, visited):
    
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    coords = [(x, y)]
	

    while q:
        x, y = q.pop()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
			# boundaries
            if 0 <= nx < 10 and 0 <= ny < a:
				# check if already visited
                if graph[ny][nx] == graph[y][x] and not visited[ny][nx]:
                    q.appendleft((nx, ny))
                    visited[ny][nx] = True
                    coords.append((nx, ny))
    return coords


def mooyo(graph):
    visited = [[False] * 10 for _ in range(a)]
    all_coords = []

    for i in range(a):
        for j in range(10):
		# check if visited
            if graph[i][j] != 0 and not visited[i][j]:
                temp = mark_connected(j, i, graph, visited)
                if len(temp) >= b:
                    all_coords += temp

    if not all_coords:
        return graph

    for x, y in all_coords:
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


ans = mooyo(c)
with open('mooyomooyo.out', 'w') as out:
	for i in ans:
		print("".join([str(x) for x in i]), file=out)