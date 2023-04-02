def solution(n, s):
    answer = []
    i = 0
    if n > s :
        answer.append(-1)
        return answer
    i = s%n
    for num in range(n):
        answer.append(s//n)
    
    for num in range(i):
        answer[num] += 1 
    
    answer.sort()
    return answer