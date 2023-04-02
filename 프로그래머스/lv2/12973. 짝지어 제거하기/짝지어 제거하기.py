def solution(s):
    s_list = list(s)
    stack = list()
    if len(s_list)%2 == 1 :
        return 0
    
    for num in range(len(s_list)):
        #print(s_list[num])
        stack.append(s_list[num])
        if len(stack) == 1:
            continue
        elif stack[len(stack)-1] == stack[len(stack)-2]:
            #print(stack)
            stack.pop()
            stack.pop()
            
    #print(stack)
    if len(stack) == 0:
        return 1
    return 0
    