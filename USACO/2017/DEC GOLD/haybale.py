import sys

sys.stdin = open("hayfeast.in", "r")
sys.stdout = open("hayfeast.out", "w")

input = sys.stdin.readline

n, m = map(int, input().split())

put = [i for i in range(n)]

way = [[*map(int,input().split())]+[i] for i in range(n)]

sorted_way, res = sorted(way, key=lambda a:a[1]), [0] * n

for i in range(n):
    res[i] = way[i][0]

def search(x):
    if put[x] == x:
        return x
    put[x] = search(put[x])
    return put[x]

def add(x, y):
    x, y = search(x), search(y)
    res[x]+= res[y]
    res[y] = 0
    put[y] = x

for i in range(n):

    out, check = sorted_way[i][1], sorted_way[i][2]

    for use in [check + 1, check - 1]:

        if 0 <= use < n and out >= way[use][1]:
            add(put[check], put[use])

    if res[put[check]] >= m: 

        print(out)
        break