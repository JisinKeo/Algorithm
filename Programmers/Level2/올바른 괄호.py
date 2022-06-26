def solution(s):
    
    stack = []
    
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                return False
            
    if len(stack)>0:
        return False
    
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True'
  
 
