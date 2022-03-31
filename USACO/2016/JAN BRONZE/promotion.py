import sys

sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")

t = sys.stdin.readline

def bessie_promotion(n):
    result = [0, 0, 0]
    diff = [0, 0, 0, 0]
    for i in range(4):
        diff[i] = n[i][1] - n[i][0]
    result[0] = diff[3] + diff[2] + diff[1]
    result[1] = diff[3] + diff[2]
    result[2] = diff[3]

    return result

a = []
for i in range(4):
    b = list(map(int, t().split()))
    a.append(b)

temp = bessie_promotion(a)
for i in temp:
    sys.stdout.write(str(i) + "\n")