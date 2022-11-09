import sys
sys.stdin = open('censor.in', 'r')
sys.stdout = open('censor.out', 'w')
t = sys.stdin.readline

s, c = t().strip(), t().strip()
ans = ""
l = len(c)

for i in s:
    ans += i
    if ans[-l:] == c:
        ans = ans[:-l]

print(ans)