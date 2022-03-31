import sys

def pathfinder(n, k, grid):
    # if k == 1
    cnt1 = 2
    a, b = 0, 0
    for i in range(n):
        if grid[i][0] == "H" or grid[n-1][i] == "H":
            a = 1
        if grid[0][i] == "H" or grid[i][n-1] == "H":
            b = 1
    cnt1 -= (a+b)

    if k == 1:
        return cnt1
    a = n-1
    # if k == 2
    all_possible2 = []
    for i in range(1, a):
        all_possible2.append(('C' * i) + ('R' * a) + ('C' * (a-i)))
        all_possible2.append(('R' * i) + ('C' * a) + ('R' * (a-i)))
    
    # print(all_possible2)
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == "H":
                temp = 0
                while temp < len(all_possible2):
                    x = all_possible2[temp]
                    # print(x)
                    if x[:i+j].count('C') == i and x[:i+j].count('R') == j:
                        all_possible2.remove(x)
                    else:
                        temp += 1
    
    # print(all_possible2)
    cnt2 = len(all_possible2)
    # print(cnt1, cnt2)
    if k == 2:
        return (cnt1 + cnt2)
    # if k == 3
    all_possible3 = []
    for i in range(1, a):
        for j in range(1, a):
            all_possible3.append(('C' * i) + ('R' * j) + ('C' * (a-i)) + ('R' * (a-j)))
            all_possible3.append(('R' * i) + ('C' * j) + ('R' * (a-i)) + ('C' * (a-j)))
    for i in range(0, n):
        for j in range(0, n):
            if grid[i][j] == "H":
                temp = 0
                while temp < len(all_possible3):
                    x = all_possible3[temp]
                    if x[:i+j].count('C') == i and x[:i+j].count('R') == j:
                        all_possible3.remove(x)
                    else:
                        temp += 1
    cnt3 = len(all_possible3)
    # print(cnt1, cnt2, cnt3)
    if k == 3:
        return (cnt1 + cnt2 + cnt3)
answers = []
a = int(sys.stdin.readline().strip())
for _ in range(a):
    b, c = map(int, sys.stdin.readline().split())
    use = []
    for _ in range(b):
        use.append(list(sys.stdin.readline().strip()))
    t = pathfinder(b, c, use)
    answers.append(t)
    # print(pathfinder(b, c, use))
for i in answers:
    print(i)