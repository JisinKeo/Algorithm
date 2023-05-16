for testcase in range(1, 11):

    length = int(input())

    word = list(input() for _ in range(8))

    if length % 2 == 0:

        cnt = 0

        check = 0

        for i in range(8):
            for j in range(8):
                for k in range(length//2):
                    if i-k>=0 and i+k+1<8:
                        if word[i-k][j] == word[i+k+1][j]:
                            check += 1
                if check == length//2:
                     cnt += 1
                check = 0
                for k in range(length//2):
                    if j-k>=0 and j+k+1<8:
                        if word[i][j-k] == word[i][j+k+1]:
                            check += 1
                if check == length//2:
                    cnt += 1
                check = 0
                

        print('#%d %d'%(testcase, cnt))

    elif length == 1:
        print('#%d %d'%(testcase, 64))

    else:

        cnt = 0

        check = 0

        for i in range(8):
            for j in range(8):
                for k in range(1, 1+length//2):
                    if i+k<8 and i-k>=0:
                        if word[i+k][j] == word[i-k][j]:
                            check += 1
                if check == length//2:
                    cnt += 1
                check = 0
                for k in range(1, 1+length//2):
                    if j+k<8 and j-k>=0:
                        if word[i][j+k] == word[i][j-k]:
                            check += 1
                if check == length//2:
                    cnt += 1
                check = 0

        print('#%d %d'%(testcase, cnt))



