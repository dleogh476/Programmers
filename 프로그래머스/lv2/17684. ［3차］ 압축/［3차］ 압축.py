
def solution(msg):
    voka = {}
    answer = []
    idx = 1
    for ap in range(ord('A'), ord('Z')+1):
        voka[chr(ap)] = idx
        idx += 1
        
    end_idx = 0
    start_idx = 0
    while start_idx != len(msg):
        flag = True
        end_idx = start_idx
        test_voka = ""
        b_voka =""        
        while flag:                                  
            if start_idx == end_idx:
                test_voka = msg[start_idx]
            else : 
                test_voka = msg[start_idx:end_idx+1]
            #단어 확인
            if voka.get(test_voka) == None: #없는 경우
                voka[test_voka] = len(voka) + 1
                answer.append(voka[b_voka])
                start_idx = end_idx
                flag = False
            else : #있는경우
                b_voka = test_voka[:]  
                end_idx += 1
                if end_idx == len(msg):
                    answer.append(voka[test_voka])
                    return answer
                
                    
    print(end_idx)
    return answer