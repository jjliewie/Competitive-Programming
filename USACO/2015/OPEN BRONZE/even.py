# fuck doesn't work and idk why

import sys
t = sys.stdin.readline

sys.stdin = open('geteven.in', 'r')
sys.stdout = open('geteven.out', 'w')

# (B+E+S+S+I+E)(G+O+E+S)(M+O+O) 
def sample(b, e, s, i, g, o, m):
    return (b+e+s+s+i+e)*(g+o+e+s)*(m+o+o)

def calc(b, e, s, i, g, o, m):
    return d["B"][b]*d["E"][e]*d["S"][s]*d["I"][i]*d["G"][g]*d["O"][o]*d["M"][m]

n = int(t().strip())
d = {}
ans = 0
for _ in range(n):
    a, b = t().split()
    if a not in d:
        d[a] = [0, 0]
    if int(b) % 2:
        d[a][0] += 1
    else: d[a][1] += 1

# B,E,S,I,G,O,M

for b in range(2):
    for e in range(2):
        for s in range(2):
            for i in range(2):
                for g in range(2):
                    for o in range(2):
                        for m in range(2):
                            tmp = sample(b, e, s, i, g, o, m)
                            if not tmp % 2:
                                ans += calc(b, e, s, i, g, o, m)

print(ans)