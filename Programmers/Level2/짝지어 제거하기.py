def solution(s):
    answer = -1
    check = []
    for x in s:
        check.append(x)
        if len(check) > 1:
            if check[-1] == check[-2]:
                check.pop()
                check.pop()
    if len(check) == 0:
        answer = 1
    else:
        answer = 0
    return answer
