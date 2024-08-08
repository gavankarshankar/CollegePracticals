def bfs(start):
    visited=[]
    queue=[start]
    vertex=[] 
    for i in graph:
        vertex.append(i)
    while queue:
        if vertex not in visited:
            visited.append(vertex)
            print(vertex)

            neighbors=graph[vertex]
            for ng in neighbors:
                if ng not in visited:
                    queue.append(ng)


graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['E']  
}

start_vertex='A'
bfs(start_vertex)