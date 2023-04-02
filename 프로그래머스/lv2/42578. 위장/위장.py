def solution(clothes):
    answer = 1
    dict_c = dict()
    
    for item_idx in range(len(clothes)):
        #print(clothes[item_idx][1])
        value = dict_c.get(clothes[item_idx][1])
        #print(value)
        if value == None:
            dict_c[clothes[item_idx][1]] = 1
            continue
        dict_c[clothes[item_idx][1]] += 1
        #print(dict_c[clothes[item_idx][1]])
    #모든 경우의 수 
    for item in dict_c.items():
        #print(item[1])
        answer *= (item[1]+1)
    
    #모두 안입는 경우의 수 삭제 
    answer -= 1
    
    return answer