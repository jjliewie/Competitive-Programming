import sys

sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

t = sys.stdin.readline

n, b = map(int, t().split())

xcoors, ycoors = [], []

locations = []

for _ in range(n):
    x, y = map(int, t().split())
    xcoors.append(x)
    ycoors.append(y)
    locations.append([x, y])

# xcoors.sort()
# ycoors.sort()

res = n 

for i in xcoors:
    for j in ycoors:

        xpartition, ypartition = i+1, j+1

        sections = [0]*4

        for a in range(n):
            x, y = locations[a][0], locations[a][1]

            if xpartition > x and ypartition > y:
                sections[0] += 1
            elif xpartition > x and ypartition < y:
                sections[1] += 1
            elif xpartition < x and ypartition > y:
                sections[2] += 1
            else:
                sections[3] += 1
            
        res = min(res, max(sections))

print(res)