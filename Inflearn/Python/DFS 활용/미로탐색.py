dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(x, y):

    global cnt

    if x == 6 and y == 6:
        cnt += 1
        return

    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < 7 and y+dy[i] >= 0 and y+dy[i] < 7:
            if maze[x+dx[i]][y+dy[i]] == 0:
                maze[x+dx[i]][y+dy[i]] = 1
                DFS(x+dx[i], y+dy[i])
                maze[x+dx[i]][y+dy[i]] = 0
    
    



if __name__=="__main__":


    maze = [list(map(int, input().split())) for _ in range(7)]

    cnt = 0

    maze[0][0] = 1

    DFS(0, 0)

    print(cnt)
