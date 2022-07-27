GRASS_TYPES = range(1, 5)	
a, b = [], []
	
with open('revegetate.in') as read:
	n, m = map(int, read.readline().split())
	
	for i in range(m):
		field1, field2 = map(int, read.readline().split())
		a.append(field1)
		b.append(field2)
		if field1 > field2:
			a[i], b[i] = b[i], a[i]

g = [0] * (n + 1)
ans = []

for i in range(1, n + 1):
	for j in GRASS_TYPES:
		bvar = True
		for k in range(m):
			if b[k] == i and g[a[k]] == j:
				bvar = False
		if bvar: 
			break
	g[i] = j
	ans.append(j)

output = "".join([str(i) for i in ans])
print(output, file=open('revegetate.out', 'w'))