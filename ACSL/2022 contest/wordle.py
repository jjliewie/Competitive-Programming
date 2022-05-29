# lol idk why I'm in the intermediate contest either... and then i got 11/20 in shorts..

n = list(input().split())
target = n[0]
guesses = n[1:]

guesses.sort()

def qual(q, idx):
    cur = [x for x in n[0]]
    s = [x for x in q]
    green, yellow = 0, 0
    g_vowels = 0
    first, last = 0, 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    if s[0] == target[0]:
        first += 1
    if s[-1] == target[-1]:
        last += 1

    for i in range(5):
        if s[i] == cur[i]:
            if s[i] in vowels:
                g_vowels += 1
            s[i] = '0'
            cur[i] = '0'
            green += 1

    for i in range(5):
        if s[i] in cur and s[i] != '0':
            cur[cur.index(s[i])] = '0'
            yellow += 1

    return [green, yellow, first, last, g_vowels, len(guesses) - idx]

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in guesses:
    for char in i:
        if char in alphabet:
            idx = alphabet.index(char)
            alphabet = alphabet[:idx] + alphabet[idx+1:]

not_included = "".join(alphabet)

res = []
for i in range(len(guesses)):
    tmp = qual(guesses[i], i)
    if tmp[0] != 0 or tmp[1] != 0:
        res.append(tmp)

res.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]), reverse=True)

ans = []

for i in res[:6]:
    t = guesses[len(guesses) - i[5]]
    if t[0] != 0 or t[1] != 0:
        ans.append(t)

if len(ans) < 6:
    print(not_included)
else: print(" ".join(ans))

'''
test case:
ports climb spots sport parts stops traps sorts porch props shots prank
'''