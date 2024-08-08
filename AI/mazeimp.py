maze=[['O','W','W'],
      [' ','W',' '],
      [' ',' ','o']]

for i in range(len(maze)):
    print(maze[i])

print(maze[2][2])

def bfs(m):
    new_m=m
    start=m[2][2]
    frontier=[start]
    visited=[start]
    while(len(frontier)>0):
        curCell=frontier.pop(0)
        print("Current cell:",curCell)
        if(curCell==(1,1)):
            break
        for i in range (len(new_m)):
            for p in range(len(new_m)):
                if(new_m[i][p]==' '):
                    #print("empty space found at",new_m.index(new_m[i][p]))
                    new_m[i][p]='+'
    for i in range(len(maze)):
        print(maze[i]) 

bfs(maze)
            