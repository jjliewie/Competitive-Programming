with open('sort.in') as read:
	n = int(read.readline())
	l, locations = [0] * n, {}

	for i in range(n):
		val = (int(read.readline()), i)
		l[i], locations[val] = val, i
    
sorted_l, ans = sorted(l), -float('inf')

for cnt, i in enumerate(sorted_l):
	ans = max(ans, locations[i] - cnt)
    
print(ans + 1, file=open('sort.out', 'w'))