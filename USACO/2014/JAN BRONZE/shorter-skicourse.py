with open('skidesign.in') as read:
    n = int(read.readline())
    elevation = [int(read.readline()) for _ in range(n)]

ans = 10 ** 10

for i in range(1, 83):
    temp = 0
    for j in elevation:
        if j < i:
            temp += (j - i) ** 2
        elif j > i + 17:
            temp += (i + 17 - j) ** 2
    ans = min(ans, temp)
    
print(ans, file=open('skidesign.out', 'w'))