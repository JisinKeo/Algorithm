def solution(numbers, hand):
    
    answer = ''
    
    left_x = 3
    left_y = 0
    right_x = 3
    right_y = 2
    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            if x == 1:
                left_x = 0
                left_y = 0
            elif x == 4:
                left_x = 1
                left_y = 0
            elif x == 7:
                left_x = 2
                left_y = 0 
            answer += 'L'
        elif x == 3 or x == 6 or x == 9:
            if x == 3:
                right_x = 0
                right_y = 2
            elif x == 6:
                right_x = 1
                right_y = 2
            elif x == 9:
                right_x = 2
                right_y = 2
            answer += 'R'
        elif x == 2 or x == 5 or x == 8 or x == 0:
            if x == 2:
                if(abs(left_x-0)+abs(left_y-1)<abs(right_x-0)+abs(right_y-1)):
                    left_x = 0
                    left_y = 1
                    answer += 'L'
                elif (abs(left_x-0)+abs(left_y-1)>abs(right_x-0)+abs(right_y-1)):
                    right_x = 0
                    right_y = 1
                    answer += 'R'
                
                else:
                    if hand == "right":
                        right_x = 0
                        right_y = 1
                        answer += 'R'                        
                    elif hand == "left":
                        left_x = 0
                        left_y = 1
                        answer += 'L'   
            elif x == 5:
                if(abs(left_x-1)+abs(left_y-1)<abs(right_x-1)+abs(right_y-1)):
                    left_x = 1
                    left_y = 1
                    answer += 'L'
                elif (abs(left_x-1)+abs(left_y-1)>abs(right_x-1)+abs(right_y-1)):
                    right_x = 1
                    right_y = 1
                    answer += 'R'
                
                else:
                    if hand == "right":
                        right_x = 1
                        right_y = 1
                        answer += 'R'                        
                    elif hand == "left":
                        left_x = 1
                        left_y = 1
                        answer += 'L'
            elif x == 8:
                if(abs(left_x-2)+abs(left_y-1)<abs(right_x-2)+abs(right_y-1)):
                    left_x = 2
                    left_y = 1
                    answer += 'L'
                elif (abs(left_x-2)+abs(left_y-1)>abs(right_x-2)+abs(right_y-1)):
                    right_x = 2
                    right_y = 1
                    answer += 'R'
                
                else:
                    if hand == "right":
                        right_x = 2
                        right_y = 1
                        answer += 'R'                        
                    elif hand == "left":
                        left_x = 2
                        left_y = 1
                        answer += 'L'
            elif x == 0:
                if(abs(left_x-3)+abs(left_y-1)<abs(right_x-3)+abs(right_y-1)):
                    left_x = 3
                    left_y = 1
                    answer += 'L'
                elif (abs(left_x-3)+abs(left_y-1)>abs(right_x-3)+abs(right_y-1)):
                    right_x = 3
                    right_y = 1
                    answer += 'R'
                
                else:
                    if hand == "right":
                        right_x = 3
                        right_y = 1
                        answer += 'R'                        
                    elif hand == "left":
                        left_x = 3
                        left_y = 1
                        answer += 'L'
    return answer
