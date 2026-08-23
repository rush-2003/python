# Fixed Size Window:
#     We do maintain window size
#     There is a window size we need to compare
    
# Variable Size Window:
#     We do not maintain window size
#     There is condition we need to compare

'''
Fixed Size Window General Format

whle j < len(arr):
    Calculations
    if window size < required size:
        j += 1 
    elif window size == required size:
        answer = max(answer, calculations)
        calculations remove i
        calculations add j
        window size maintained and slide
        
return answer
'''

'''
Variable Size Window General Format

whle j < len(arr):
    Calculations
    if Condition < Given Condition:
        j += 1 
    elif Condition == Given Condition:
        answer = calculations
        calculations add j
    elif Condition > Given Condition:
        while Condition > Given Condition:
            calculations remove i
            i += 1
        j += 1
        calculations add j
        window size maintained and slide
        
return answer
'''