import sys
t = sys.stdin.readline

n = int(t())
arr = []
for i in range(n):
    arr.append([*map(int, t().split())])
arr.sort()
ans, cnt = 0, 0
for a, b in arr:
    cnt += a
    ans += (b-cnt)
print(ans)