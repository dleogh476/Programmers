def solution(nums):
    answer = 0
    take_phonekemon_num = len(nums)/2
    types_of_phonekemon = []
    
    for num in nums:
        if num in types_of_phonekemon:
            continue
        types_of_phonekemon.append(num)
        answer += 1
    
    type_len = len(types_of_phonekemon)    
    if type_len > take_phonekemon_num:
        answer = take_phonekemon_num
    else:
        answer = type_len
        
    return answer