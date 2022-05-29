'''

red: hours
green: minutes
blue: seconds

yellow: hours + minutes
cyan: minutes + seconds
magenta: hours + seconds
white: hours + minutes + seconds

minutes + seconds: x5 [0-55]

hours: (0, 11)
minutes: (0, 55)
seconds: (0, 55)

sqaures in clock: 2 (1 x 1), 1 (2 x 2), 1 (3 x 3), 1 x (5 x 5)

'''

from itertools import product

def which(i):
    if i == 0 or i == 1:
        return 1
    if i == 2:
        return 2
    if i == 3:
        return 3
    if i == 4:
        return 5

d = {
    'r': [1, 0, 0], 
    'g': [0, 5, 0], 
    'b': [0, 0, 5], 
    'y': [1, 5, 0], 
    'c': [0, 5, 5], 
    'm': [1, 0, 5], 
    'w': [1, 5, 5], 
    'k': [0, 0, 0]
}

def check(pos, h, m, s):
    h1, m1, s1 = 0, 0, 0

    for i in range(len(pos)):
        h1 += d[pos[i]][0] * which(i)
        m1 += d[pos[i]][1] * which(i)
        s1 += d[pos[i]][2] * which(i)
    
    return h1 == h and m1 == m and s1 == s

n = input()

h, m, s = map(int, n.split(":"))

all = product(['r', 'g', 'b', 'y', 'c', 'm', 'w', 'k'], repeat=5)

ans = []

for i in all:
    if check(i, h, m, s):
        ans.append("".join(i))

ans.sort()

print(" ".join(ans))