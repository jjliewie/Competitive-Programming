import sys

sys.stdin = open("revegetate.in", "r")
sys.stdout = open("revegetate.out", "w")

input = sys.stdin.readline

n, m = map(int, input().split())

a, b, g = [0] * 151, [0] * 151, [0] * 101

for i in range(m):
    a[i], b[i] = map(int, input().split())
    if a[i] > b[i]:
        a[i], b[i] = b[i], a[i]
for i in range(1, n + 1):
    for j in range(1, 5):
        bvar = True
        for k in range(m):
            if b[k] == i and g[a[k]] == j:
                bvar = False
        if bvar: 
            break
    g[i] = j
    print(j, end="")
    
print()