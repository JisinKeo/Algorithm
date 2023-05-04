dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt

    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < n and y+dy[i] >= 0 and y+dy[i] < n:
            if apart[x+dx[i]][y+dy[i]] == 1 and check[x+dx[i]][y+dy[i]] == 0:
                check[x+dx[i]][y+dy[i]] = 1
                cnt += 1
                DFS(x+dx[i], y+dy[i])
                

if __name__=="__main__":

    n = int(input())

    apart = [list(map(int, input())) for _ in range(n)]

    check = [[0] * n for _ in range(n)]

    cnt = 1

    result = []

    for i in range(n):
        for j in range(n):
            if apart[i][j] == 1 and check[i][j] == 0:
                check[i][j] = 1
                DFS(i, j)
                result.append(cnt)
                cnt = 1
                
    print(len(result))
    
    result.sort()
    
    for x in result:
        print(x)
                

