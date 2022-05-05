import sys

sys.stdin = open("word.in", "r")
sys.stdout = open("word.out", "w")
input = sys.stdin.readline

def bessie_word(n, k, t):
    n_list = t.split()
    result = [n_list[0]]
    cur_idx = 0
    word_cnt = len(result[cur_idx])
    for i in range(1, n):
        if len(n_list[i]) + word_cnt > k:
            cur_idx += 1
            word_cnt = len(n_list[i])
            result.append(n_list[i])
        else:
            result[cur_idx] += " " + n_list[i]
            word_cnt = len(n_list[i]) + word_cnt
    return result

a, b = map(int, input().split())
c = input()
temp = bessie_word(a, b, c)
for i in temp:
    print(i)