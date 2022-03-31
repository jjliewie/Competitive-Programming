import sys

sys.stdin = open("photo.in", "r")
sys.stdout = open("photo.out", "w")

t = sys.stdin.readline

def farmer_photoshoot(n, k):

    result = [0]*1001
    for i in range(1, k[0]):
        temp = []
        result[0] = i
        ok = True
        for j in range(1, n):
            result[j] = k[j-1] - result[j-1]
            if result[j] in temp or result[j] <= 0:
                ok = False
                break
            temp.append(result[j])
        if ok:
            return result[0:n]

a = int(t())
b = list(map(int, t().split()))

use = farmer_photoshoot(a, b)

for i in range(len(use)):
    use[i] = str(use[i])
print(" ".join(use))