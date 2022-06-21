def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    
    for x in new_id:
        if x.isalpha() or x.isdigit() or x in ['-','_','.']:
            answer += x
            
    while '..' in answer:
        answer = answer.replace('..','.')
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
        
    if answer == '':
        answer += 'a';
    if len(answer) >= 16:
        answer = answer[:15]
        
    if answer[-1] == '.':
        answer = answer[:-1]
        
    while len(answer) < 3:
        answer += answer[-1]
 
    return answer
