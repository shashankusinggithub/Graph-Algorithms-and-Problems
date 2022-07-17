class Graph:
    def __init__(self):
        self.listOfGraph = []
    # adding edges with s = source, d = destination, w = weight
    def addEdge(self, s,d,w):
        self.listOfGraph.append([s,d,w])



# n = no of vertices
# iterating it to n-1 times 
# after n-1 check with another loop, if values are still changing it means its stuck in infinite -ve cycle 
def bellmanFord(graph, s,e, n):
    dist = [float("inf")]* n
    dist[s] = 0

    for _ in range(n-1):
        print(dist)
        for u, v, w in graph:
            if dist[u] != float("inf") and dist[v] > dist[u] + w:
                dist[v]=dist[u] + w
            
    for u, v, w in graph:
            if dist[u] != float("inf") and dist[v] > dist[u] + w:
                return -1
    
    else: return sum(dist)

if __name__ == "__main__":
    g = Graph()

    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(2, 3, -5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    gra = g.listOfGraph
    print(bellmanFord(gra, 0,4,5))