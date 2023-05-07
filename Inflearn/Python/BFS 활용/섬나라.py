from collections import deque

n = int(input())

island = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

check = [[0]*n for _ in range(n)]

cache = deque()

cnt = 0

for i in range(n):
    for j in range(n):
        if island[i][j] == 1 and check[i][j] == 0:
            check[i][j] = 1
            cache.append((i,j))
            while cache:
                now = cache.popleft()
                for x in range(8):
                    for y in range(8):
                        if now[0]+dx[x]>=0 and now[0]+dx[x]<n and now[1]+dy[y]>=0 and now[1]+dy[y]<n:
                            if island[now[0]+dx[x]][now[1]+dy[y]] == 1 and check[now[0]+dx[x]][now[1]+dy[y]] == 0:
                                cache.append((now[0]+dx[x],now[1]+dy[y]))
                                check[now[0]+dx[x]][now[1]+dy[y]] = 1
            cnt += 1


print(cnt)
