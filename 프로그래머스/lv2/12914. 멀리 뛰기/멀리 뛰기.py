def solution(n):
    answer = 0
    frist = 1
    second = 2
    
    if n == frist:
        return frist%1234567
    elif n == second:
        return second%1234567
    
    for num in range(n-2):
        answer = frist + second
        frist = second
        second = answer
    return answer%1234567

