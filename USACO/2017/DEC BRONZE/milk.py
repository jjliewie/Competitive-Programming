import sys

sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

input = sys.stdin.readline

milk = [7] * 3
numeric = {'Bessie' : 0, 'Elsie' : 1, 'Mildred' : 2}

measurements = []
cur = 7
ans = 0

n = int(input())
for _ in range(n):
	a, b, c = input().split()
	measurements.append((int(a), b, int(c)))

measurements.sort()
 
def dist_max():
    res = 0
    for i in range(3):
        if milk[i] == max(milk):
            res += (2**i)
    return res

for date, name, amt in measurements:

	milk[numeric[name]] += amt
	new = dist_max()

	if cur != new:
		ans += 1
		cur = new
		
print(ans)