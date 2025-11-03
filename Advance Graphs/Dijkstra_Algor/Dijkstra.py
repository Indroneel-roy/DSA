import heapq
class Solution:
    def dijkstra(self, graph, start):
        distances = {node : float('inf') for node in graph}
        distances[start] = 0
        minH = [(0, start)]  # (distance, node)
        while minH:
            current_distance, current_node = heapq.heappop(minH)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(minH, (distance, neighbor))
        return distances
    
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    sol = Solution()
    start_node = 'A'
    distances = sol.dijkstra(graph, start_node)
    print(f"Shortest distances from node {start_node}: {distances}")    