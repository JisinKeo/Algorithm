import sys
from collections import deque

n, L, R = map(int, sys.stdin.readline().split())

egg = []
for i in range(n):
    egg.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, checked):
    dq = deque()
    dq.append((x, y))
    region = [(x, y)]
    egg_sum = egg[x][y]
    checked[x][y] = True

    while dq:
        curx, cury = dq.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not checked[nx][ny]:
                if L <= abs(egg[nx][ny] - egg[curx][cury]) <= R:
                    checked[nx][ny] = True
                    dq.append((nx, ny))
                    region.append((nx, ny))
                    egg_sum += egg[nx][ny]

    return region, egg_sum

result = 0

while True:
    checked = [[False] * n for _ in range(n)]
    move_occurred = False

    for i in range(n):
        for j in range(n):
            if not checked[i][j]:
                region, egg_sum = bfs(i, j, checked)
                if len(region) > 1:
                    move_occurred = True
                    new_egg_value = egg_sum // len(region)
                    for x, y in region:
                        egg[x][y] = new_egg_value

    if not move_occurred:
        break

    result += 1

print(result)
