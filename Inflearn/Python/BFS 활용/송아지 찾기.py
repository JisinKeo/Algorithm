'''
현수는 송아지를 잃어버렸다. 다행히 송아지에는 위치추적기가 달려 있다. 
현수의 위치와 송아 지의 위치가 직선상의 좌표 점으로 주어지면 현수는 현재 위치에서 송아지의 위치까지 다음과 같은 방법으로 이동한다.
현수는 스카이 콩콩을 타고 가는데 한 번의 점프로 앞으로 1, 뒤로 1, 앞으로 5를 이동할 수 있다. 
최소 몇 번의 점프로 현수가 송아지의 위치까지 갈 수 있는지 구하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 현수의 위치 S와 송아지의 위치 E가 주어진다. 직선의 좌표 점은 1부터 10,000 까지이다.

▣ 출력설명
점프의 최소횟수를 구한다.

▣ 입력예제 1 
5 14

▣ 출력예제 1 
3
'''
from collections import deque

MAX = 10000
check = [0] * (MAX + 1)
distance = [0] * (MAX + 1)
n, m = map(int, input().split())

cache = deque()
cache.append(n)
check[n] = 1
distance[n] = 0

while cache:
    now = cache.popleft()
    if now == m:
        break

    for i in (now+1, now-1, now+5):
        if 1<=i<=MAX:
            if check[i] == 0:
                cache.append(i)
                distance[i] = distance[now] + 1
                check[i] = 1
print(distance[m])
