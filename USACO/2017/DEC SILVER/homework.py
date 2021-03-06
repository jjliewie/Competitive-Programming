import sys

sys.stdin = open("homework.in", "r")
sys.stdout = open("homework.out", "w")

input = sys.stdin.readline

n = int(input())

questions = [*map(int, input().split())]

left, right, total, minimum, ans = -1, n, [0] * n, [0] * n, []

total[n - 1], minimum[n - 1] = questions[n - 1], questions[n - 1]

for i in range(n - 2, 0, -1):

    cur_q = questions[i]

    total[i], minimum[i] = cur_q + total[i + 1], min(minimum[i + 1], cur_q)

    cur_s, tmp = total[i] - minimum[i], (n - (i + 1))

    if cur_s * right > left * tmp:
        left, right = cur_s , tmp
        ans = [i]

    elif cur_s * right == left * tmp:
        ans.append(i)

for k in sorted(ans):
    print(k)