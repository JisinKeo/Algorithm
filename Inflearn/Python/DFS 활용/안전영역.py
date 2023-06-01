import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sys.setrecursionlimit(10**6)

def DFS(i, j, height):
    global check
    for a in range(4):
        if 0 <= i+dx[a] < n and 0 <= j+dy[a] < n:
            if water[i + dx[a]][j + dy[a]] > height and check[i + dx[a]][j + dy[a]] == 0:
                check[i + dx[a]][j + dy[a]] = 1
                DFS(i + dx[a], j + dy[a], height)


if __name__ == "__main__":

    n = int(input())
    water = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    for height in range(1, 101):
        cnt = 0
        check = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if water[i][j] > height and check[i][j] == 0:
                    cnt += 1
                    DFS(i, j, height)
        result = max(cnt, result)

    print(result)
