import random
import itertools
path=[]
def dfs(visited,graph,node):
    print('Current node:',node)
    if node not in visited:
        path.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            print(node,'neighbour:',neighbour)
            dfs(visited,graph,neighbour)
    else:
         print(node,'is visited.')

    #print('Path is',path)

visited=set()
graph1={
    'D':['C','A','E'],
    'E':['A','D'],
    'C':['A','D'],
    'A':['B','C','D','E'],
    'B':['A']  
}

dfs(visited,graph1,'D')
print('Path is',path)

#print(graph)
# Convert dictionary items to a list of tuples
items = list(graph1.items())

#print("DFS:")
#dfs(visited,graph,'D')
