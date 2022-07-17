
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adjlist):
        import heapq

        visited = set()
        mindist = {x:float('inf') for x in range(V)}
    
        mindist[0] = 0    
        q = []
        heapq.heappush(q, (0,0))
        
        while q:
            dis, curr = heapq.heappop(q)
            visited.add(curr)
            for node, distance in adjlist[curr]:
                if node not in visited and distance < mindist[node]:
                    mindist[node] = distance
                    heapq.heappush(q, (distance, node))
        return sum(mindist.values())
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = 1
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends