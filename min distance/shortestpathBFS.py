from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        
        self.listOFGraph = []

    def addEdge(self, node1, node2, weight=1):
        self.listOFGraph.append([node1,node2,weight])
    
    def adjacencyMatrix(self):
        dic = defaultdict(list)
        for x in self.listOFGraph:
            dic[x[0]].append((x[1], x[2]))
        # print(dic)
        return dic
        
def bfs(g, s, e):
    q = deque()
    q.append(s)
    visited = {s:"start"}
    while q:
        
        
        temp = q.popleft()
        print(temp, end=" ")
        if temp == e:
            print(visited)
            order = []
            revpath(visited,e, order)
            print(order)
            return visited

        for x in g[temp]:
            if x[0] not in visited:
                q.append(x[0])
                visited[x[0]] = (temp,x[1])

def revpath(visited, e, order):
    temp = visited[e]
    order.append(e,)
    
    while temp != "start":
        
        order.append(temp)
        temp = visited[temp[0]]
        
    return order  

    



if __name__ == "__main__":
    graph = Graph(6)
    graph.addEdge(0,1,5)
    graph.addEdge(0,2,3)
    graph.addEdge(1,3,1)
    graph.addEdge(1,4,15)
    graph.addEdge(4,2,7)
    graph.addEdge(4,5,7)
    graph.addEdge(3,5,100)
    print(graph.listOFGraph)
    # g = graph.adjacencyMatrix()
    # bfs(g,0, 3)