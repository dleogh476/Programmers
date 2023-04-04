def solution(want, number, discount):
    answer = 0
    discount_map= {}
    want_map = {}
    
    for idx,w in enumerate(want):
        want_map[w] = number[idx]

    for num in range(len(discount)-9):
        discount_map.clear()
        for idx in range(num,(num+10)):
            if want_map.get(discount[idx]) == None:
                break
            elif discount_map.get(discount[idx]) == None: 
                discount_map[discount[idx]] = 1
            else :
                discount_map[discount[idx]] += 1 
                if want_map[discount[idx]] < discount_map[discount[idx]]:
                    discount_map.clear()
                    break
        sum = 0
        for a in discount_map:
            sum += discount_map[a]
        if sum == 10:
            answer +=1 
    return answer