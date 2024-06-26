import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

moving = list(map(int, sys.stdin.readline().split()))

dq = deque()

# [안정성, 사람 있는지 여부]
for i in range(2*n):
    dq.append([moving[i], 0])

result = 0

while True:
    result += 1

    # 1. 무빙워크가 한 칸 회전합니다.
    dq.rotate(1)
    dq[n-1][1] = 0  # n번 칸에 사람이 있다면 내리기

    # 2. 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한 칸 이동할 수 있으면 이동합니다. 
    for i in range(n-2, -1, -1):
        if dq[i][1] == 1 and dq[i+1][1] == 0 and dq[i+1][0] > 0:
            dq[i+1][1] = 1
            dq[i+1][0] -= 1
            dq[i][1] = 0

    dq[n-1][1] = 0  # n번 칸에 사람이 있다면 내리기

    # 3. 1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.
    if dq[0][1] == 0 and dq[0][0] > 0:
        dq[0][1] = 1
        dq[0][0] -= 1

    # 안정성이 0인 칸의 개수를 셈
    zero_stability_count = sum(1 for x in dq if x[0] == 0)

    # 4. 안정성이 0인 칸이 k개 이상이라면 과정을 종료합니다.
    if zero_stability_count >= k:
        break    

print(result)
