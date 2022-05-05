import sys
t = sys.stdin.readline
_ = int(t())
ans = 0
for i in sorted(map(int, t().split()))[::-1]:
    if ans <= i: 
        ans += 1
print(ans)