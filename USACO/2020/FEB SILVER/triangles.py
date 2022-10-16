import sys

# sys.stdin = open('triangles.in', 'r')
# sys.stdout = open('triangles.out', 'w')

t = sys.stdin.readline

def solution():
    n = int(t())
    fieldx, fieldy = [[] for _ in range(20001)], [[] for _ in range(20001)]
    allcoors = []

    for _ in range(n):
        x, y = map(int, t().split())
        fieldx[x+10000].append(y+10000)
        fieldy[y+10000].append(x+10000)
        allcoors.append((x+10000, y+10000))
    
    for i in range(20001):
        fieldx[i].sort()
        fieldy[i].sort()
    
    psumx, psumy = [[] for _ in range(20001)], [[] for _ in range(20001)]
    
    for i in range(20001):
        xl, yl = len(fieldx[i]), len(fieldy[i])
        psumx[i], psumy[i] = {}, {}
        if xl > 1:
            temp = sum(fieldx[i]) - xl * fieldx[i][0]
            psumx[i][fieldx[i][0]] = temp
            for j in range(xl-1):
                temp += (2 * (j+1) - xl) * (fieldx[i][j+1] - fieldx[i][j])
                psumx[i][fieldx[i][j+1]] = temp

        if yl > 1:
            temp = sum(fieldy[i]) - yl * fieldy[i][0]
            psumy[i][fieldy[i][0]] = temp
            for j in range(yl-1):
                temp += (2 * (j+1) - yl) * (fieldy[i][j+1] - fieldy[i][j])
                psumy[i][fieldy[i][j+1]] = temp
    
    ans = 0
    for a in allcoors:
        x, y = a
        if not psumx[x] or not psumy[y]:
            continue
        ans += abs(psumx[x][y] * psumy[y][x]) 
        
    return ans % (int(1e9+7))

print(solution())