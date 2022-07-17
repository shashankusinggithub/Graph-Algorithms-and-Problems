# Python Program for Floyd Warshall Algorithm
 
# Number of vertices in the graph
V = 4
 
# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = float("inf")
 
# Solves all pair shortest path
# via Floyd Warshall Algorithm
 
def floydWarshall(graph):
    
    dist = graph #list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(V):
 
        # pick all vertices as source one by one
        for i in range(V):
 
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
 
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    print(dist)
 
 
# A utility function to print the solution
def printSolution(dist):
    print ("Following matrix shows the shortest distances\
 between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print ("%7s" % ("INF"),end=" ")
            else:
                print ("%7d\t" % (dist[i][j]),end=' ')
            if j == V-1:
                print ()
 
 
# Driver program to test the above program
# Let us create the following weighted graph

graph = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
# Print the solution
floydWarshall(graph)
# This code is contributed by Mythri J L