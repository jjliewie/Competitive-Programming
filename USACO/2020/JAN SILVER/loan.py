import sys
import math

sys.stdin = open("loan.in", "r")
sys.stdout = open("loan.out", "w")

input = sys.stdin.readline

n, k, m = map(int, input().split())

def check_which(mid):

    g, cur = 0, k
    
    while g < n and cur:
        y = math.floor((n - g) / mid)

        if y <= m:
            g += m * cur
            break

        calc = min(math.floor((n - mid * y - g) / y + 1), cur)

        g += y * calc
        cur -= calc

    return g >= n

low, high = 1, n + 1

while low + 1 < high:

    middle = low + high >> 1
    if check_which(middle):
        low = middle
    else:
        high = middle

print(low)