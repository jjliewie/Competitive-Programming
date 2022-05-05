import sys

sys.stdin = open("citystate.in", "r")
sys.stdout = open("citystate.out", "w")

input = sys.stdin.readline

a = int(input())
cities = {}
for i in range(a):
    city, state = input().split()

    city = city[:2]

    if city == state:
        continue

    key = city+state

    if key in cities:
        cities[key] += 1
    else:
        cities[key] = 1
    
ans = 0
for i in cities.keys():
    use = i[2:] + i[:2]
    if use in cities:
        ans += (cities[i] * cities[use])

print(ans//2)