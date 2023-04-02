def solution(operations):
    answer = [0,0]
    #minmaxLoc = [0,0]
    queue = list()
    #b = list()
    
    #for a in operations:
        #명령어와 값 분리
    #    b.append(a.split(" "))
    #print(b)    
    
    for op in operations:
        b = op.split(" ")
        b[1] = int(b[1])
        if b[0] == 'I': #추가
            print(queue)
            if len(queue) == 0 :
                queue.append(b[1])
                continue
                
            if b[1] < queue[len(queue) - 1]:
                queue.append(b[1])
                continue
                
            for idx,val in enumerate(queue):
                if b[1] > val:
                    queue.insert(idx, b[1])
                    break             
        elif b[0] == 'D': #삭제
            if b[1] == 1: #max 삭제
                if len(queue) == 0:
                    continue
                queue.pop(0)
            elif b[1] == -1: #min 삭제
                if len(queue) == 0:
                    continue
                queue.pop(-1)
    if len(queue) == 0:   
        return answer
    elif len(queue) == 1:
        c = queue.pop(0)
        answer[0] = c
        answer[1] = c
        return answer
    else :
        c = queue.pop(0)
        d = queue.pop(-1)
        answer[0] = c
        answer[1] = d
        return answer
    #print(op_list)
    