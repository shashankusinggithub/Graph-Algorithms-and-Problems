from collections import defaultdict
import heapq

def adjacencyList(g):
    dic = defaultdict(list)
    for x in g:
        dic[x[0]].append((x[1], x[2]))    
    return dic

def dijkstras(graph, s, e):
    visited = set()             #s et to store visited
    dist = { x:[float('inf'), None] for x in range(6)}  #dictionary to add all the mindistances default set to inf
    pq = [] # pq is min heap
    dist[s] = [0, None] # initialising starting node min distance to 0
    heapq.heappush(pq, (s, 0))  # pushing it into heap
    while pq:
        index, minvalue = heapq.heappop(pq)
        visited.add(index)
        if index == e:
            return dist
        for edge, cost in graph[index]:
            if edge not in visited :
                newDist = cost + dist[index][0]
                if dist[edge][0] > newDist:
                    dist[edge] = [newDist, index]
                    
                    heapq.heappush(pq, (edge, newDist))
    return -1


if __name__ == "__main__":
    g = [[2, 0, -3],[0, 1, 5],  [1, 2, -4], [1, 4, 15], [4, 2, 7], [4, 5, 7], [3, 5, 100]]
    graph = adjacencyList(g)
    print(dijkstras(graph,0,5))