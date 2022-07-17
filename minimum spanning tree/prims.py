import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        key=[float('inf')]*(V) # assigning max value to key this is wher all the distances are stores
        
        visited=[False]*(V) # assigning False to visited all nodes        
        
        par=[-1]*(V) #parents list default is -1
        
        key[0]=0        # assiging 0 or distance from source or source to 0
        par[0]=-1       # assiging -1 as parent
        l=[]            # heapq
        heapq.heappush(l,(0,0))
        while l:
            di,curr=heapq.heappop(l)
            visited[curr]=True
            for i in adj[curr]: # adj[curr] - all the nodes connected to curr
                node=i[0] 
                d=i[1]      #distance from curr to node
                if not visited[node] and d<key[node]: # if node is not visited and key[node] is less tha distance
                    par[node]=curr      
                    key[node]=d
                    heapq.heappush(l,(key[node],node))
                    
        return sum(key)  




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

# test case
# 3 3
# 0 1 5
# 1 2 3
# 0 2 1