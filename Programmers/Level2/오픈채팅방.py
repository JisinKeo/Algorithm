def solution(record):
    answer = []
    dict = {}
    for i in range(len(record)):
        temp = record[i].split(' ')
        if temp[0] == 'Enter':
            dict[temp[1]] = temp[2]
        elif temp[0] == 'Change':
            dict[temp[1]] = temp[2]
        
    for i in range(len(record)):
        temp = record[i].split(' ')
        if temp[0] == 'Enter':
            answer.append(dict[temp[1]] + "님이 들어왔습니다.")
        elif temp[0] == 'Leave':
            answer.append(dict[temp[1]] + "님이 나갔습니다.")
    return answer
