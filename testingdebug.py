class Solution:
    
	def findMotherVertex(self, V, adj):
	    visited = {}	
            
        for vertex in range(V):
            tmpvisited = set()
            self.dfs(adj, vertex,tmpvisited, visited)
            visited[vertex] = list(tmpvisited)
            print(tmpvisited)
            if V == len(visited[vertex]):
                
                return vertex
        else:
            return -1
	def dfs(self, adj, node, tmpvisited, visited):
	    tmpvisited.add(node)
	   # print(visited)
	    for y in adj[node]:
	        if y in visited:
	            tmpvisited.update(visited[y])
	            continue
	        else:
	            self.dfs(adj, y, tmpvisited, visited)
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
	T=1
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		obj = Solution()
		ans = obj.findMotherVertex(V, adj)
		print(ans)
# } Driver Code Ends