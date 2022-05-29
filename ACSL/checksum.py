i = int(input())

def sumd(n):
    t = [int(x) for x in str(n)]
    return sum(t)

def clone(l):
    copy = l[:]
    return copy

def cs(n):
    tmp = n[::-1]
    ans = tmp[0]
    for i in range(1, len(tmp), 2):
        k = tmp[i] * 2
        if k > 9: 
            tmp[i] = sumd(k)
        else: tmp[i] = k
    val = sum(tmp) - ans
    val *= 9
    val %= 10
    return val == ans

def ta(n, idx):
    n[idx] = min(n[idx] + 1, 9)
    if cs(n): return n
    n[idx] = max(n[idx] - 2, 0)
    if cs(n): return n

    return []

ver = [int(x) for x in str(i)]

if cs(ver):
    print("VALID")
else:
    for v in range(len(ver)):
        copy = clone(ver)
        cur = ta(copy, v)
        if cur:
            string = "".join([str(i) for i in cur])
            print(int(string))
            break
