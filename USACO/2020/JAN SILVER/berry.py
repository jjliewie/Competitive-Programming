import sys

sys.stdin = open("berries.in", "r")
sys.stdout = open("berries.out", "w")

input = sys.stdin.readline

n, k = map(int, input().split())

berries = [*map(int, input().split())]

maximum, ans = max(berries), 0

for i in range(1, maximum + 1):
    mod, full, tmp = i, 0, 0

    for j in range(n):
        full += berries[j] // mod
    if full < k / 2:
        break
    if full >= k:
        ans = max(ans, (k / 2) * i)
        continue
    idx = (full - k / 2) * i
    berries.sort(key = lambda x: (x % mod), reverse=True)

    while tmp < (k - full):
        if tmp < len(berries):
            idx += berries[tmp] % mod
            tmp += 1
        else:
            break

    ans = int(max(ans, idx))

print(ans)