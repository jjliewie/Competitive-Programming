import sys
input = sys.stdin.readline

n = int(input())
recipe = [[] for _ in range(n + 1)]

a = [0] + list(map(int, input().split()))
k = int(input())

for _ in range(k):
    res, _, *ingredients = map(int, input().split())
    recipe[res] += ingredients

def work(cur):
    second = a.copy()
    second[-1] -= cur
    for i in range(n, 0, -1):
        if second[i] >= 0: 
            continue
        if not recipe[i]: 
            return False
        for j in recipe[i]:
            second[j] += second[i]
    return True

# binary search
l, h = 0, sum(a)
while l <= h:
    m = (l + h) // 2
    if work(m): 
        l = m + 1
    else: 
        h = m - 1
print(h)