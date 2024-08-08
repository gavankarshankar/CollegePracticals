from pyamaze import maze,agent,textLabel,COLOR


def bfs(m):
    start=(m.rows,m.cols)
    print('Start =',start)
    visited=[start]
    frontier=[start]
    bfsPath={}
    bSearch=[]
    while len(frontier)>0:
        curCell=frontier.pop(0)
        print("Current cell:",curCell)
        if(curCell==(1,1)):
            break
        for direction in 'ESNW':
            if m.maze_map[curCell][direction]==True:
                if direction=='E':
                    childCell=(curCell[0],curCell[1]+1)
                elif direction=='W':
                    childCell=(curCell[0],curCell[1]-1)
                elif direction=='N':
                    childCell=(curCell[0]-1,curCell[1])
                elif direction=='S':
                    childCell=(curCell[0]+1,curCell[1])
                if childCell in visited:
                    continue
                frontier.append(childCell)
                print("frontier:",frontier)
                visited.append(childCell)
                print("visisted:",visited)
                bfsPath[childCell]=curCell
                bSearch.append(childCell)
    print("bfspath:",bfsPath)
    fwdpath={}
    cell=(1,1)
    while cell!=start:
        fwdpath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdpath

m=maze(5,5)
m.CreateMaze()
bSearch,bfsPath,fwdpath=bfs(m)
a=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=False)
#c=agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
c=agent(m,1,1,footprints=True,color=COLOR.green,shape='square',filled=True,goal=(m.rows,m.cols))
m.tracePath({a:bSearch},delay=390)
m.tracePath({c:bfsPath},delay=390)
print(m.maze_map)
a=agent(m,footprints=True)
path=bfs(m)
print("\nfwdpath is ",path)
m.tracePath({a:path})
m.run()




