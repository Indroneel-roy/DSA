class bellman_fort:
    def __init__(self, v):
        self.v = v
        self.edges = []
        
    def add_edges(self, u, v, w):
        self.edges.append((u, v, w))
    
       
    
    def bellman_ford(self, src):
        dis = [float('inf')] * self.v
        dis[src] = 0
        for _ in range(self.v - 1):
            for u, v, w in self.edges:
                if dis[u] != float('inf') and dis[u] + w < dis[v]:
                    dis[v] = dis[u] + w 
        
        # Check for negative weight cycles
        for u, v, w in self.edges:
            if dis[u] != float('inf') and dis[u] + w < dis[v]:
                print("Graph contains negative weight cycle")
                return                  
        
        print("Vertex Distance from Source")
        for i in range(self.v):
            print(f"{i}\t\t{dis[i]}")
if __name__ == "__main__":
    g = bellman_fort(5)
    g.add_edges(0, 1, -1)
    g.add_edges(0, 2, 4)
    g.add_edges(1, 2, 3)
    g.add_edges(1, 3, 2)
    g.add_edges(1, 4, 2)
    g.add_edges(3, 2, 5)
    g.add_edges(3, 1, 1)
    g.add_edges(4, 3, -3)
    
    g.bellman_ford(0)            