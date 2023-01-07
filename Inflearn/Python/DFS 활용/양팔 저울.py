'''


만약 추의 무게가 {1, 5, 7}이면 S=13이고, 그릇에 담을 수 있는 물의 무게는 {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13}이고, 
1부터 S사이에서 무게에서 9와 10에 대응하는 무게의 물을 담을 수 없다.
K(3<=K<=13)개의 추 무게가 주어지면, 1부터 S사이의 정수 중 측정이 불가능한 물의 무게는 몇 가지가 있는 지 출력하는 프로그램을 작성하세요.


▣ 입력설명
첫 번째 줄에 자연수 K(3<=K<=13)이 주어집니다.
두 번째 줄에 K개의 각 추의 무게가 공백을 사이에 두고 주어집니다. 각 추의 무게는 1부터 200,000까지이다.
▣ 출력설명
첫 번째 측정이 불가능한 가지수를 출력하세요.
▣ 입력예제 1 
3
1 5 7
▣ 출력예제 1 
2

'''

def DFS(v, presentWeight):
   

    if v+1 == k:
        if 0 < presentWeight and presentWeight <= weightSum:
            chk.add(presentWeight)
        return
    

    DFS(v+1, presentWeight+weight[v])
    DFS(v+1, presentWeight-weight[v])
    DFS(v+1, presentWeight)
    

if __name__=="__main__":
    k = int(input())
    weight = list(map(int, input().split()))
    weightSum = sum(weight)

    chk = set()
    
    DFS(-1, 0)
    print(weightSum - len(chk))
