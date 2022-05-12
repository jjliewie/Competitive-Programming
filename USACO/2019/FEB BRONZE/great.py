a, b, g = [0] * 151, [0] * 151, [0] * 101
	
with open('revegetate.in') as read:
	n, m = map(int, read.readline().split())
	
	for i in range(m):
		a[i], b[i] = map(int, read.readline().split())
		if a[i] > b[i]:
			a[i], b[i] = b[i], a[i]

ans = []

for i in range(1, n + 1):
	for j in range(1, 5):
		bvar = True
		for k in range(m):
			if b[k] == i and g[a[k]] == j:
				bvar = False
		if bvar: 
			break
	g[i] = j
	ans.append(j)
    
with open('revegetate.out', 'w') as out:
    output = "".join([str(i) for i in ans])
    print(output, file=out)