h, p, s = 0, 0, 0
gestures = []

with open('hps.in') as r:
    n = int(r.readline().strip())
    for _ in range(n):
        gesture = r.readline().strip()
        if gesture == 'H': h += 1
        elif gesture == 'P': p += 1
        else: s += 1
        gestures.append([h, p, s])

ans = -float('inf')

for i in range(n):
    empty = [0, 0, 0]
    for j in range(3):
        empty[j] = gestures[-1][j] - gestures[i][j]
    ans = max(ans, max(gestures[i]) + max(empty))

print(ans, file=open('hps.out', 'w'))