import sys

sys.stdin = open("sort.in", "r")
sys.stdout = open("sort.out", "w")

input = sys.stdin.readline

n, fix = int(input()), 111111
l, locations = [0] * n, {}

for i in range(n):
    idx = int(input()) * fix + i
    l[i], locations[idx] = idx, i
    
sorted_l, ans = sorted(l), -float('inf')

for cnt, i in enumerate(sorted_l):
  
    ans = max(ans, locations[i] - cnt)
    
print(ans + 1)