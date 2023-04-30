from collections import deque

maze = [list(map(int, input().split())) for _ in range(7)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

distance = [[0] * 7 for _ in range(7)]
check = [[0] * 7 for _ in range(7)]

position = deque()

position.append((0,0))

ex = 0 

while position:

    if ex == 1:
        break

    length = len(position)

    for i in range(length):

        now = position.popleft()


        for j in range(4):
            if now[0]+dx[j]>=0 and now[0]+dx[j]<7 and now[1]+dy[j]>=0 and now[1]+dy[j]<7:
                if now[0]+dx[j] == 6 and now[1]+dy[j] == 6:
                    distance[now[0]+dx[j]][now[1]+dy[j]] = distance[now[0]][now[1]] + 1
                    ex = 1
                elif maze[now[0]+dx[j]][now[1]+dy[j]] == 0 and check[now[0]+dx[j]][now[1]+dy[j]] == 0:
                    distance[now[0]+dx[j]][now[1]+dy[j]] = distance[now[0]][now[1]] + 1
                    check[now[0]+dx[j]][now[1]+dy[j]] = 1
                    position.append((now[0]+dx[j],now[1]+dy[j]))
            

if ex == 0:
    print("-1")
else:
    print(distance[6][6])
