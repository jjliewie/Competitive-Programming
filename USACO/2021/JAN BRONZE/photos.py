import sys
input = sys.stdin.readline

n = int(input())
even, odd = 0, 0

cows = [*map(int, input().split())]

for c in cows:
    if c % 2 == 0: even += 1
    else: odd += 1

while odd > even:
    odd -= 2
    even += 1

if even > odd + 1: even = odd + 1
print(even + odd)