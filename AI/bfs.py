from collections import deque
def bfs(graph,start):
    visited = set()
    queue=deque([start])
    while queue:
        vertex=queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex,end=" => ")
            #Explore neighbours
            neighbours=graph[vertex]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['E']  
}

start_vertex='F'
bfs(graph,start_vertex)