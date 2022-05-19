from collections import deque

fullness, que = set(), deque()
fullness.add((0, 0))
que.append((0, 0))

with open('feast.in') as r:
    T, A, B = map(int, r.readline().split())

while que:
    node = que.pop()
    cur, not_full = node[0], node[1]
    for fruit in (A, B):
        if not not_full:
            # drink water
            water = (cur // 2, 1 - not_full)
            if water not in fullness:
                que.appendleft(water)
                fullness.add(water)
        # eat lemon or oranges
        after = cur + fruit
        if after <= T and (after, not_full) not in fullness:
            que.appendleft((after, not_full))
            fullness.add((after, not_full))
            
max_fullness = max([_[0] for _ in fullness]) 
print(max_fullness, file=open('feast.out', 'w'))