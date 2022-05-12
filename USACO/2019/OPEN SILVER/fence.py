with open('fenceplan.in') as read:
    n, m = map(int, read.readline().split())
    connection = [[] for _ in range(n)]
    coors = [[*map(int, read.readline().split())] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, read.readline().split())
        connection[x - 1].append(y - 1)
        connection[y - 1].append(x - 1)

visited = [0] * n
ans = float('inf')

for i in range(n):
    if not visited[i]:
        queue, visited[i] = [i], 1

        ax = bx = coors[i][0]
        ay = by = coors[i][1]

        for node in queue:
            for conn in connection[node]:
                if not visited[conn]:
                    visited[conn] = 1
                    
                    cur_x, cur_y = coors[conn]

                    ax, ay = min(ax, cur_x), min(ay, cur_y)
                    bx, by = max(bx, cur_x), max(by, cur_y)

                    queue.append(conn)

        ans = min(ans, ((bx + by) - (ax + ay)) * 2)

print(ans, file=open('fenceplan.out', 'w'))