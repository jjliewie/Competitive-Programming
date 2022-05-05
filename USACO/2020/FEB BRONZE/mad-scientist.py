import sys

sys.stdin = open("breedflip.in", "r")
sys.stdout = open("breedflip.out", "w")

t = sys.stdin.readline

def flip(a, b, k):
    for i in range(a, b+1):
        if k[i] == "H":
            k = k[:i] + "G" + k[i+1:]
        else:
            k = k[:i] + "H" + k[i+1:]
    return k

def mad_scientist(n, k):
    cnt = 0
    start, end = -1, -1
    for i in range(len(k)):
        if k[i] == n[i]:
            if end > -1:
                k = flip(start, end, k)
                cnt += 1
            end = -1
            start = -1
        else:
            if start == -1:
                start = i
                end = i
            else:
                end = i
    return cnt

_ = int(t())
a = t()
b = t()
print(mad_scientist(a, b))