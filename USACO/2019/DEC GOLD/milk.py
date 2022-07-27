# partial but this is probably the best possible solution (for python) since it works on other sites (not usaco)

import sys

sys.stdin = open("milkvisits.in", "r")
sys.stdout = open("milkvisits.out", "w")

t = sys.stdin.readline
from bisect import bisect_left

n, m = map(int, t().split())
farms = [*map(int, t().split())]

length = 1 << n.bit_length()

way = [[] for _ in range(length * 2)]

path, pre = [[] for _ in range(n)], [[] for _ in range(n)]

length = 2 ** n.bit_length()

k, bot, top, v, vals = [0] * n, [0] * n, [0] * n, [0] * n, [0] * n

full, half = [-1] * n, [-1] * n

res = []

tmp = -1

def change(f1, f2, f3):

	result = 0

	while(top[f1] != top[f2]):

		if full[top[f1]] < full[top[f2]]:
			f1, f2 = f2, f1

		current = top[f1]
        
		result |= use(bot[current], bot[f1], f3)

		if result:
			return 1

		f1 = half[current]

	if full[f1] > full[f2]:
		f1, f2 = f2, f1

	result |= use(bot[f1], bot[f2], f3)

	return result
	
def before(x):
	v[x] = 1
	for j in path[x]:
		if v[j]:
			continue
		v[j] = 1
		pre[x].append(j)
		before(j)

def start():
	for i in range(n):
		way[i + length].append(vals[i])

	for i in range(length - 1, 0, -1):
		way[i] = sorted(way[i * 2] + way[i * 2 + 1])

def use(x, y, z):
	x += length; y += length
	result = 0
	while x <= y:
		if x % 2 == 1:
			idx = bisect_left(way[x], z)
			if idx < len(way[x]) and way[x][idx] == z:
				return 1
			x += 1
		if y % 2 == 0:
			idx = bisect_left(way[y], z)
			if idx < len(way[y]) and way[y][idx] == z:
				return 1
			y -= 1
		x //= 2; y //= 2
	return result

def dfs(x):
	k[x] = 1
	idx = 0
	for i in pre[x]:
		full[i] = full[x] + 1
		half[i] = x
		dfs(i)
		k[x] += k[i]
		if k[i] > k[pre[x][0]]:
			pre[x][0], pre[x][idx] = pre[x][idx], pre[x][0]
		idx += 1
	
def stop(x):
    global tmp

    tmp += 1
    bot[x] = tmp
    
    for after in pre[x]:

        if after == pre[x][0]:
            top[after] = top[x]

        else:
            top[after] = after

        stop(after)

for i in range(n-1):
	a, b = map(int, t().split())
	path[a-1].append(b-1)
	path[b-1].append(a-1)

before(0)
dfs(0)
stop(0)

for i in range(n):
	vals[bot[i]] = farms[i]

start()

for i in range(m):

	a, b, c = map(int, t().split())
	res.append(change(a - 1, b - 1, c))

print("".join([str(i) for i in res]))