'''
최소힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요. 
1) 자연수가 입력되면 최소힙에 입력한다.
2) 숫자 0 이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다.
(출력할 자료가 없으면 -1를 출력한다.) 
3) -1이 입력되면 프로그램 종료한다.
▣ 입력설명
첫 번째 줄부터 숫자가 입력된다. 입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정수형 범위에 있다.
▣ 출력설명
2) 연산을 한 결과를 보여준다.
'''



import heapq as hq

a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))

    else:
        hq.heappush(a, n)
