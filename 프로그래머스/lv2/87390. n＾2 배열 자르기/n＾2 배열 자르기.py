def solution(n, left, right):
    answer = []
    for idx in range(right - left + 1):
        number = left + idx
        if (number//n) >= (number%n):
            answer.append((number//n) + 1)
        else :
            answer.append((number%n) + 1)
    #print(answer)
    return answer