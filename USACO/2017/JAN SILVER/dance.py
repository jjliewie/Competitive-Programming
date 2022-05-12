import heapq

with open('cowdance.in') as r:
    n, maximum = map(int, r.readline().split())
    dance = [int(r.readline()) for _ in range(n)]

left, right = 1, n + 1

while left < right:
    mid = (left + right) // 2
    parts = dance[:mid]
    heapq.heapify(parts)
    
    for i in range(mid, n): 
        tmp = heapq.heappop(parts) + dance[i]
        heapq.heappush(parts, tmp)

    if maximum < max(parts): 
        left = mid + 1
    else: 
        right = mid

print(left, file=open('cowdance.out', 'w'))