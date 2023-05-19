n = int(input())

valley = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * n for _ in range(n)]

dx = [-1, 0]
dy = [0, -1]

result[0][0] = valley[0][0]

for i in range(1, n):
    result[i][0] = valley[i][0] + result[i-1][0]
for j in range(1, n):
    result[0][j] = valley[0][j] + result[0][j-1]

for i in range(1, n):
    for j in range(1, n):
        min_num = 10000000
        for k in range(2):
            if 0 <= i+dx[k] < n and 0 <= j+dy[k] < n:
                if result[i+dx[k]][j+dy[k]] < min_num:
                    min_num = result[i+dx[k]][j+dy[k]]
        result[i][j] = min_num + valley[i][j]

print(result[n-1][n-1])
