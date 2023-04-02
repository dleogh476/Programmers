def a(numbers, target,floor,val):
    target_count = 0
     
    #base
    if floor == len(numbers): 
        if val == target:
            return 1
        else :
            return 0
    valp = val + numbers[floor] 
    valm = val - numbers[floor]
    target_count += a(numbers, target, floor + 1,valp)
    target_count += a(numbers, target, floor + 1,valm)
    
    return target_count

def solution(numbers, target):
    answer = 0
    mem = {}
    answer = a(numbers, target,0,0)
    return answer