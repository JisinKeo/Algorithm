'''

방향그래프가 주어지면 1번 정점에서 N번 정점으로 가는 모든 경로의 가지 수를 출력하는 프로그램을 작성하세요. 

아래 그래프에서 1번 정점에서 5번 정점으로 가는 가지 수는 총 6 가지입니다.

1 2 3 4 5
1 2 5
1 3 4 2 5
1 3 4 5
1 4 2 5
1 4 5

그래프에서 경로란 방문한 노드는 중복해서 방문하지 않습니다.

▣ 입력설명

첫째 줄에는 정점의 수 N(2<=N<=20)와 간선의 수 M가 주어진다. 그 다음부터 M줄에 걸쳐 연결정보가 주어진다.

▣ 출력설명

총 가지 수를 출력한다.
'''

def DFS(v):

    global cnt

    if v == n:
        cnt += 1
        return

    for i in range(1, n+1):
        if graph[v][i] == 1 and check[i] == 0:
            check[i] = 1
            DFS(i)
            check[i] = 0



if __name__=="__main__":
    n, m = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    check = [0] * (n+1)
    for i in range(m):
        start, end = map(int, input().split())
        graph[start][end] = 1

    cnt = 0
    check[1] = 1
    DFS(1)

    print(cnt)
