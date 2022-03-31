import sys

sys.stdin = open("marathon.in", "r")
sys.stdout = open("marathon.out", "w")

t = sys.stdin.readline

def total_distance(n, coors):
    t_distance = 0
    coors_x = coors[0][0]
    coors_y = coors[0][1]
    for i in range(1, n):
        t_distance += (abs(coors_x - coors[i][0]) + abs(coors_y - coors[i][1]))
        coors_x = coors[i][0]
        coors_y = coors[i][1]
    return t_distance

def calculate_distance(k, i, tdistance):
    distance = tdistance

    distance -= (abs(k[i][0] - k[i-1][0]) + abs(k[i][1] - k[i-1][1]) + abs(k[i][0] - k[i+1][0]) + abs(k[i][1] - k[i+1][1]))
    distance += (abs(k[i-1][0] - k[i+1][0]) + abs(k[i-1][1] - k[i+1][1]))

    return distance

def bessie_check(n, k):
    distance = float('inf')
    tdistance = total_distance(n, k)
    for i in range(1, n-1):
        distance = min(distance, calculate_distance(k, i, tdistance))
    return distance

n = int(t())
temp_list = []
for i in range(n):
    a, b = map(int, t().split())
    k = [a, b]
    temp_list.append(k)

ans = bessie_check(n, temp_list)

sys.stdout.write(str(ans))