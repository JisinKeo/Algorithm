for testcase in range(1, 11):

    n = int(input())

    table = [list(map(int, input().split())) for _ in range(n)]
    
    cnt = 0

    for j in range(100):

        state = 2

        for i in range(100):
            if table[i][j] == 1 and state == 2:
                state = 1
            elif table[i][j] == 2 and state == 2:
                continue
            elif table[i][j] == 1 and state == 1:
                continue
            elif table[i][j] == 2 and state == 1:
                cnt += 1
                state = 2
    
    print("#%d %d"%(testcase, cnt))
