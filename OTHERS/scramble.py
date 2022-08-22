from itertools import permutations
import enchant

d = enchant.Dict("en_US")

word = input()
word_list = [c for c in word]

all = permutations(word_list)

for i in all:
    temp = "".join(i)
    if d.check(temp):
        print(temp)
        break