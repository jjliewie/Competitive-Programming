import sys
input = sys.stdin.readline
n = int(input())
d = {}

for _ in range(n):
    q = input().strip().split()
    if q[0] == "1":
        if q[1] in d:
            print(d[q[1]])
        else: print("0")
        continue
    d[q[1]] = q[2]