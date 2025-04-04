from collections import defaultdict
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.row = len(graph)
    
    def searching_algo_BFS(self, s,t, parent):
        visited = [False] * (self.row)
        queue = []
        
        queue.append(s)
        visited[s] = True 
        
        while queue:
            u = queue.pop(0)
            
            
            for i, val in enumerate(self.graph[u]):
                if visited[i] == False and val > 0:
                    visited[i] = True 
                    queue.append(i)
                    parent[i] = u 
        return True if visited[t] else False
    
    def Ford_Fulkerson(self, source, sink):
        parent = [-1] * (self.row)
        max_flow = 0
        
        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]    
            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Max Flow: %d " % g.Ford_Fulkerson(source, sink))            
           