nv = 4
INF = 999

def floyd_algo(G):
    distance = [row[:] for row in G]
    
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    printing_the_solution(distance)        
 
def printing_the_solution(distance):
    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end= " ")
        print(" ")

if __name__ == "__main__":
    G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
    floyd_algo(G)
                