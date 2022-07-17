from collections import defaultdict
#Initializing the Graph Class
class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices
    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)


    #Implementing Topological Sort
    def topogologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topogologicalSortUtil(i, visited, stack)
            
        stack.insert(0, v)
        
    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topogologicalSortUtil(k, visited, stack)
            
        print(stack)

if __name__ == "__main__":
    tempGraph = Graph(8)
    tempGraph.addEdge("A", "C")
    tempGraph.addEdge("C", "E")
    tempGraph.addEdge("E", "H")
    tempGraph.addEdge("E", "F")
    tempGraph.addEdge("F", "G")
    tempGraph.addEdge("B", "D")
    tempGraph.addEdge("B", "C")
    tempGraph.addEdge("D", "F")

    tempGraph.topologicalSort()

    #Output
    # ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']