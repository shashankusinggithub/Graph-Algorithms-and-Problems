class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # searching and compressing the tree updating the parent array
    def search(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] =  self.search(parent, parent[i])
    
    # creating the union or assigning the roots to each node to check if they are connected
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        #  rank or height of the root is used to reduce /
        #  complexity, parent with higher node is assidgned as root
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
    # if rank are same one of the is assigned as root and rank is increased
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            self.search(parent, u)
            self.search(parent, v)
            x = parent[u]
            y = parent[v]
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:",u, v,end =" ")
            print("-",weight)
 
 
g = Graph(5)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)
g.kruskal()