from collections import deque

n = int(input())

arr = [list(map(int ,input().split())) for _ in range(n)]

check = [[0] * n for _ in range(n)]

mid = n//2

sum = 0

cache = deque()

cache.append((mid, mid))

check[mid][mid] = 1

sum = sum + arr[mid][mid]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

count = 0

while True:

    if count == mid:
        break

    cache_length = len(cache)


    for j in range(cache_length):

        now = cache.popleft()

        for i in range(4):

            if now[0]+dx[i] >= 0 and now[0]+dx[i] < n and now[1]+dy[i] >= 0 and now[1]+dy[i] < n:
                if check[now[0]+dx[i]][now[1]+dy[i]] == 0:
                    cache.append((now[0]+dx[i], now[1]+dy[i]))
                    check[now[0]+dx[i]][now[1]+dy[i]] = 1
                    sum = sum + arr[now[0]+dx[i]][now[1]+dy[i]]
                
    count += 1
    
print(sum)
