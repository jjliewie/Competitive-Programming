import sys

sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

input = sys.stdin.readline

def farmer_triangle(n, k):
    double_max = 0
    for i in range(n):
        t = k[:i] + k[i+1:]
        max_x = 0
        max_y = 0
        for j in range(len(t)):
            if t[j][0] == k[i][0]:
                temp_x = abs(t[j][1] - k[i][1])
                max_x = max(temp_x, max_x)
            elif t[j][1] == k[i][1]:
                temp_y = abs(t[j][0] - k[i][0])
                max_y = max(temp_y, max_y)
        double_area = max_x * max_y
        double_max = max(double_max, double_area)
    return double_max

a = int(input())
b = []
for i in range(a):
    p, q = map(int, input().split())
    b.append([p, q])
print(farmer_triangle(a, b))
