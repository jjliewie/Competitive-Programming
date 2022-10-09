import sys
t = sys.stdin.readline

n, k = map(int, t().split())
hay = [0] * (n+1)

for _ in range(k):
    a, b = map(int, t().split())
    for i in range(a, b+1):
        hay[i] += 1

print(sorted(hay)[(n+1)//2])