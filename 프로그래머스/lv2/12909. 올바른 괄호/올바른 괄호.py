def solution(s):
    answer = True
    s_list = list(s)
    lp_stack = []
    
    for a in s_list:
        if '(' == a:
            lp_stack.append('(')
        elif ')' == a :
            if len(lp_stack) == 0:                
                return False
            elif lp_stack:
                lp_stack.pop()
                
    if len(lp_stack) != 0:
        return False
    
    return True