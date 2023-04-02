def solution(n):
    c = bin(n).count('1')
    for num in range(n+1,1000001):
        if bin(num).count('1') == c:
            return num