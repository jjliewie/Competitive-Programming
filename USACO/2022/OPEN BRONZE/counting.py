import sys
t = sys.stdin.readline

def solution():

    n = int(t())
    g, l, ans = [], [], float('inf')
    for _ in range(n):
        a, b = t().split()
        if a=="G": g.append(int(b))
        else: l.append(int(b))
        
    bessie = g+l + [l[0] -1] + [g[-1] + 1]

    for i in range(len(bessie)):

        tmp = 0

        for greater in g:
            if bessie[i] < greater: tmp += 1
        for less in l:
            if bessie[i] > less: tmp += 1
        
        ans = min(tmp, ans)
    
    return ans

print(solution())