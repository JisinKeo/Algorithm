dx = [0, 0]
dy = [1, -1]


def DFS(i, j, start):

    if i > 9:
        return

    check[i][j] = 1

    if ladder[i][j] == 2:
        print(start)
        return

    dfs_check = 0

    for a in range(2):
        if 0 <= i + dx[a] < 10 and 0 <= j + dy[a] < 10:
            if ladder[i + dx[a]][j + dy[a]] == 1 and check[i + dx[a]][j + dy[a]] == 0:
                dfs_check = 1
                DFS(i + dx[a], j + dy[a], start)
    if dfs_check == 0:
        DFS(i + 1, j, start)


if __name__ == "__main__":

    ladder = [list(map(int, input().split())) for _ in range(10)]

    for start in range(10):
        check = [[0] * 10 for _ in range(10)]
        if ladder[0][start] == 1:
            DFS(1, start, start)
