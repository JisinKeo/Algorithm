from itertools import permutations


def solution(A, B):
    
    answer = 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    i = 0
    j = 0
    
    while i < len(A):
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            i += 1

    
    return answer
