dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def DFS(a, b):
    global count
    for i in range(4):
        na = a + dx[i]
        nb = b + dy[i]
        if na>=0 and na<n and nb>=0 and nb<m:
            if pos[na][nb] == 0:
                pos[na][nb] = 1
                count += 1
                DFS(na, nb)
        else:
            continue
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b, d = map(int, input().split())
    count = 1
    pos = [list(map(int, input().split())) for _ in range(n)]
    pos[a][b] = 1
    DFS(a, b)

    print(count)
