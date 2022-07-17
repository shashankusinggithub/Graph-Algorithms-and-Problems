def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x]) # tree compresttion technique        



def union( a, b):
    find(a)
    find(b)
    yRoot = parent[b]
    xRoot = parent[a]

    if xRoot == yRoot:
        return 
    
    if rank[xRoot] < rank[yRoot]:
        parent[xRoot] = yRoot
    elif rank[xRoot] > rank[yRoot]:
        parent[yRoot] = xRoot
    else:
        parent[yRoot] = xRoot
        rank[xRoot] +=1

N = 10 # no of vertices
parent = [i for i in range(N)]
rank = [0 for i in range(N)]

union(1,2)
union(2,4)
union(4,6)


