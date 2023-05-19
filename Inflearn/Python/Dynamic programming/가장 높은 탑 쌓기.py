n = int(input())

bricks = []

for _ in range(n):
    w, h, e = map(int, input().split())
    bricks.append((w, h, e))
bricks.sort(reverse=True)

dy = [0] * n
dy[0] = bricks[0][1]

for i in range(1, n):
    max_num = 0
    for j in range(0, i):
        if dy[j] > max_num and bricks[i][2] <= bricks[j][2]:
            max_num = dy[j]
    dy[i] = max_num + bricks[i][1]

print(max(dy))
