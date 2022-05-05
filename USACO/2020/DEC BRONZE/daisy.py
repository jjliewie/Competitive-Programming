def bessie_daisy(n, t):

    result = 0

    for i in range(n):
        for j in range(i, n):
            temp = 0
            d_dict = {}
            for k in range(i, j+1):
                if t[k] in d_dict.keys():
                    d_dict[t[k]] += 1
                else:
                    d_dict[t[k]] = 1
                temp += t[k]
            if (temp/(j+1-i)) in d_dict.keys() and d_dict[temp/(j+1-i)] > 0:
                result += 1

    return result

a = int(input())
b = []
temp = input().split()
for i in range(a):
    b.append(int(temp[i]))

print(bessie_daisy(a, b))