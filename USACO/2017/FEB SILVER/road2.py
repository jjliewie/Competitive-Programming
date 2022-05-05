import sys

sys.stdin = open("maxcross.in", "r")
sys.stdout = open("maxcross.out", "w")

input = sys.stdin.readline

n, k, b = map(int, input().split())

id, left, right, tmp =[0] * (n + 1), 1, k, 0

for _ in range(b):
    id[int(input())] = 1

for i in range(left, right + 1):
    tmp += id[i]

possible = [tmp]

while n > right:

    tmp += id[right + 1] - id[left]

    left, right = left + 1, right + 1

    possible.append(tmp)

print(min(possible))