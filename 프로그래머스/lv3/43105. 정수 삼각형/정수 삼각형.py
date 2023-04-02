
def solution(triangle):
    memo = dict()
    answer = sum_max(triangle, 0, 0, memo)
    return answer

def sum_max(triangle ,floor, col, memo):
    a = 0
    length = floor + 1
    #base
    if floor == len(triangle) - 1:
        return triangle[floor][col]
    
    if (floor,col) in memo:
        return memo[(floor,col)]
    
    #일반적인 경우
    l = sum_max(triangle, floor+1, col,memo)
    r = sum_max(triangle, floor+1, col+1,memo)
    a = max(l, r) + triangle[floor][col]
    
    memo[(floor,col)] = a
    
    return a