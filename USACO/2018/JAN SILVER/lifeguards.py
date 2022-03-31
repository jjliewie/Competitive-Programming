import sys

sys.stdin = open("lifeguards.in", "r")
sys.stdout = open("lifeguards.out", "w")

t = sys.stdin.readline

n = int(t())

if n == 1:
    sys.stdout.write(str(0))
    exit()

sweep = []
for _ in range(n):
    a, b = map(int, t().split())
    sweep.append([a, b])

sweep.sort(key=lambda x:x[0])
temp = sweep[0][1]
cover = sweep[0][1] - sweep[0][0]

find_min = [0]*n

for i in range(len(sweep)):
    find_min[i] = sweep[i][1]-sweep[i][0]

cnt = 1

for start, end in sweep[1:]:
    if temp > start:
        cover += max(0, end-temp)
        find_min[cnt-1] -= (temp - start) 
        find_min[cnt] -= (min(temp, end)-start)
    else: cover += end-start

    temp = max(end, temp)
    cnt += 1

ans = cover - max(min(find_min), 0)

sys.stdout.write(str(ans))