import sys
t = sys.stdin.readline

n, k = map(int, t().split())
hay, add = [0] * (n+1), [0] * (n+1)

for _ in range(k):
  a, b = map(int, t().split())

  # we will be storing the differences!!

  hay[a] += 1
  if b < n:
    hay[b+1] -= 1

cur_sum = 0

for i in range(n+1):
  cur_sum += hay[i]
  add[i] = cur_sum

print(sorted(add)[(n+1)//2])