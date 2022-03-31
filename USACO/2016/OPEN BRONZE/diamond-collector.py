import sys

sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

t = sys.stdin.readline

a, b = map(int, t().split())

diamonds = []

for _ in range(a):
    diamonds.append(int(t()))
diamonds.sort()

res = 0

for i in range(a):
    for j in range(i+1, a):
        if diamonds[j] - diamonds[i] <= b:
            if j == a-1:
                temp = j-i+1
                res = max(res, temp)
        else:
            temp = j-i
            res = max(res, temp)
            break

print(res)

