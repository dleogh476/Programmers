def solution(k, tangerine):
    answer = 0
    dict_t = dict()
    total = 0
    for t in tangerine:
        value = dict_t.get(t)
        #귤의 크기가 없을 경우
        if value == None:
            dict_t[t] = 1
            continue
        #귤의 크기가 있을 경우
        dict_t[t] += 1
        
    #value기준으로 오름차순 정렬
    #dict_t.sort() <- 안됨
    dict_t_sort = sorted(dict_t.items(), key= lambda item : item[1], reverse = True)
    #print(dict_t_sort)
    
    #들어가나는 종류의 갯수
    for keyAndValue in dict_t_sort:
        #print(keyAndValue[0], keyAndValue[1])
        answer += 1
        total += keyAndValue[1]
        if k <= total:
            return answer
    
    return answer