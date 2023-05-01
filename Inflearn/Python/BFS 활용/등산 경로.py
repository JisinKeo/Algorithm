dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def DFS(x, y):
    global cnt

    if x == end_x and y == end_y:
        cnt += 1

    for i in range(4):
        if x+dx[i] >= 0 and x+dx[i] < n and y+dy[i] >= 0 and y+dy[i] < n:
            if check[x+dx[i]][y+dy[i]] == 0 and height[x+dx[i]][y+dy[i]] > height[x][y]:
                check[x+dx[i]][y+dy[i]] = 1
                DFS(x+dx[i], y+dy[i])
                check[x+dx[i]][y+dy[i]] = 0
                




if __name__=="__main__":

    n = int(input())
    height = [[0] * n for _ in range(n)]
    check = [[0] * n for _ in range(n)]

    max = -2147000000
    min = 2147000000

    cnt = 0

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] > max:
                max = tmp[j]
                end_x = i
                end_y = j
            if tmp[j] < min:
                min = tmp[j]
                start_x = i
                start_y = j
            height[i][j] = tmp[j]        

    check[start_x][start_y] = 1
    DFS(start_x, start_y)
    print(cnt)
