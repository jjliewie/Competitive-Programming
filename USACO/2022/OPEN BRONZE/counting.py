n = int(input())

g, l, ans = [], [], float('inf')

for _ in range(n):

    a, b = input().split()

    '''
	The position is stored in g if the cow claims that Bessie is hiding at a location greater than b.
	The position is stored in l if the cow claims that Bessie is hiding at a location less than b.
	'''

    if a == "G": 
        g.append(int(b))
    else: 
        l.append(int(b))
        
bessie = g+l + [l[0] - 1] + [g[-1] + 1]

for i in range(len(bessie)):

    tmp = 0

    ''' 
	If the cow claims that Bessie is hiding at a greater location
	but their position is greater than our position, the cow is lying.
	Vice versa, if the cow claims that Bessie is hiding at a lesser location
	but their position is lesser than our position, the cow is lying.
	'''
        
    for greater in g:
        if bessie[i] < greater: 
            tmp += 1
    for less in l:
        if bessie[i] > less: 
            tmp += 1
        
    ans = min(tmp, ans)
    
print(ans)