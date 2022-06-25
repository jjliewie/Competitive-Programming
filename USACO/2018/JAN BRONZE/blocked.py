import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

input = sys.stdin.readline

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

if x3 <= x1 and x2 <= x4:
    
    if y3 < y2 and y2 < y4: 
        y2 = y3
    if y1 < y4 and y3 < y1: 
        y1 = y4

if y3 <= y1 and y2 <= y4:

    if x3 < x2 and x2 < x4: 
        x2 = x3
    if x1 < x4 and x3 < x1:
        x1 = x4 

ans = (x2 - x1) * (y2 - y1)

print(ans)