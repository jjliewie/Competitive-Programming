with open('snowboots.in') as r:
    n, b = map(int, r.readline().split())
    depth = list(map(int, r.readline().split()))
    max_depth = [[*map(int, r.readline().split())] for _ in range(b)]

stor = [[0] * b for _ in range(n)]
stor[0][0] = 1

for i in range(n):
	cur = -1
	for j in range(b):
		s, d = max_depth[j]
		if s >= depth[i]:
			for k in range(1, d + 1):
				if stor[i - k][j] and i - k >= 0:
					stor[i][j] = 1
					cur = j
					break
		if cur != -1: break
	for j in range(cur + 1, b):
		s, d = max_depth[j]
		if s >= depth[i]: stor[i][j] = 1
for i in range(b):
	if stor[-1][i]:
		print(i, file=open('snowboots.out', 'w'))
		exit()