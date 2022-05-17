res = [[0] * 11 for _ in range(11)]
left, right, down, up = [0] * 10, [0] * 10, [0] * 10, [0] * 10

ans = [0] * 10

for i in range(1, 10):
    left[i], up[i] = 1e9, 1e9
    right[i], down[i] = -1, -1

with open('art.in') as read:
    input = read.readline
    n = int(input().strip())
    for i in range(n):
        tmp = [int(x) for x in input().strip()]
        for j in range(n):
            res[i][j] = tmp[j]
            if res[i][j]:
                use = res[i][j]
                left[use], right[use] = min(left[use], j), max(right[use], j)
                down[use], up[use] = max(down[use], i), min(up[use], i)
                ans[use] = 1

for i in range(1, 10):
    for j in range(int(up[i]), int(down[i] + 1)):
        for k in range(int(left[i]), int(right[i] + 1)):
            if res[j][k] != i:
                ans[res[j][k]] = 0

print(sum(ans), file=open('art.out', 'w'))

# res = [[0] * 11 for _ in range(11)]
# left, right, down, up = [0] * 10, [0] * 10, [0] * 10, [0] * 10

# ans = [0] * 10

# for i in range(1, 10):
#     left[i], up[i] = 1e9, 1e9
#     right[i], down[i] = -1, -1

# n = int(input().strip())

# for i in range(n):
#     tmp = [int(x) for x in input().strip()]
#     for j in range(n):
#         res[i][j] = tmp[j]
#         if res[i][j]:
#             use = res[i][j]
#             left[use], right[use], down[use], up[use] = min(left[use], j), max(right[use], j), max(down[use], i), min(up[use], i)
#             ans[use] = 1

# for i in range(1, 10):
#     for j in range(int(up[i]), int(down[i] + 1)):
#         for k in range(int(left[i]), int(right[i] + 1)):
#             if res[j][k] != i:
#                 ans[res[j][k]] = 0

# print(sum(ans))