n, l = map(int, input().split())
citations = sorted([*map(int, input().split())], reverse=True)
length = len(citations)

while citations[length - 1] < length and length >= 0:
    length -= 1

cur_h, length = length, len(citations)

if cur_h is not n:
    for i in range(cur_h, -1, -1):
        if i <= cur_h - l:
            break
        citations[i] += 1

citations.sort(reverse=True)     
while citations[length - 1] < length and length >= 0:
    length -= 1

print(length)