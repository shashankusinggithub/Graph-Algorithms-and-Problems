class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    def add2node(self,node, visited):
        #edge cases
        if node == None:
            return None
        elif node.val in visited:
            return visited[node.val]
        
        #creating clone with new neighbors
        new = Node(node.val)        
        new.neighbors = [Node(x.val) for x in node.neighbors]
        visited[node.val] = new

        #iterating it through neighnours of node and assigning it to clone created
        for i,x in enumerate(node.neighbors):                      
            new.neighbors[i] = self.add2node(node.neighbors[i], visited)    
        return new
    

    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}        
        new = self.add2node(node, visited)
        return new

