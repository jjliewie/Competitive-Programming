MX = 100002
x, c = [0] * MX, [0] * MX

with open('reststops.in') as read:
	l, n, f, b = map(int, read.readline().split())
	
	for i in range(1, n + 1):
		x[i], c[i] = map(int, read.readline().split())

ans = 0

for i in range(n, 0, -1):
	c[i] = max(c[i], c[i + 1])
	ans += (x[i] - x[i - 1]) * (f - b) * (c[i])

print(ans, file=open('reststops.out', 'w'))