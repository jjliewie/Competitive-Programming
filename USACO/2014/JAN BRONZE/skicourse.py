import sys

sys.stdin = open("skidesign.in", "r")
sys.stdout = open("skidesign.out", "w")

t = sys.stdin.readline

def cost_calculate(n, k, maximum, minimum):
    cost = 0
    for i in range(n):
        if k[i] > maximum:
            cost += ((maximum - k[i])**2)
        if k[i] < minimum:
            cost += ((k[i]-minimum) **2)
    return cost

def solution(n, k):
    answer = float('inf')
    for i in range(84):
        answer = min(answer, cost_calculate(n, k, i+17, i))
    return answer


n = int(t())
temp_list = []
for i in range(n):
    k = int(t())
    temp_list.append(k)

print(solution(n, temp_list))