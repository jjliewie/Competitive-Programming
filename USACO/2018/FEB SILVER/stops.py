import sys

sys.stdin = open("reststops.in", "r")
sys.stdout = open("reststops.out", "w")

input = sys.stdin.readline

x, c = [0] * 100005, [0] * 100005

l, n, f, b = map(int, input().split())

ans = 0

for i in range(1, n+1):
    x[i], c[i] = map(int, input().split())

for i in range(n, 0, -1):
    c[i] = max(c[i], c[i+1])
    ans += (x[i] - x[i-1]) * (f - b) * (c[i])

print(ans)