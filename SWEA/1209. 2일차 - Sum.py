for testcase in range(1, 11):
    n = int(input())

    integer = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    for i in range(100):

        cache = 0
        
        for j in range(100):
            cache += integer[i][j]

        if cache > result:
            result = cache

    for j in range(100):

        cache = 0
        
        for i in range(100):
            cache += integer[i][j]

        if cache > result:
            result = cache

    cache = 0
    
    for i in range(100):

        cache += integer[i][i]

    if cache > result:
        result = cache

    cache = 0

    for i in range(100):
        cache += integer[i][100-(i+1)]

    if cache > result:
        result = cache

    print("#%d %d"%(testcase, result))
