import sys
from itertools import combinations
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(comb):

    distance = [[1e9] * n for _ in range(n)]

    dq = deque()

    count = 0

    for hx, hy in comb:
        dq.append((hx, hy))
        distance[hx][hy] = 0

    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if distance[nx][ny] > distance[x][y] + 1:
                    distance[nx][ny] = distance[x][y] + 1
                    dq.append((nx, ny))
    for person in people:
        count += distance[person[0]][person[1]]
    return count

n, m = map(int, sys.stdin.readline().split())

city = []

for i in range(n):
    city.append(list(map(int, sys.stdin.readline().split())))

hospitals = []
people = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            hospitals.append((i, j))
        elif city[i][j] == 1:
            people.append((i, j))

result = 1e9

for comb in combinations(hospitals, m):
    result = min(result, bfs(comb))

print(result)


