capacity, milk = [0] * 3, [0] * 3
with open('mixmilk.in') as read:
    for i in range(3):
        capacity[i], milk[i] = map(int, read.readline().split())
i = 0
for _ in range(100):
    j = (i + 1) % 3
    amt = min(milk[i], capacity[j] - milk[j])
    milk[i] -= amt
    milk[j] += amt
    i = j
with open('mixmilk.out', 'w') as out:
    for fin in milk:
        print(fin, file=out)