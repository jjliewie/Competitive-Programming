import sys
t = sys.stdin.readline

n = int(t())

def factor(a, b):
    res = []
    for i in range(a, 0, -1):
        if b % i == 0:
            res.append(i)
    return res

def solution():
    x = int(t())
    k = list(map(int, t().split()))
    s = sum(k)
    possible = factor(x, s)

    for i in possible:
        v, num, use = 0, s/i, 0

        while use < x:
            v += k[use]

            if v == num:
                use += 1
                v = 0
            elif v > num: break
            elif v < num: use += 1
        
        if use == x:
            return x-i

    return -1

ans = []
for _ in range(n):
    ans.append(solution())

for i in ans:
    print(i)