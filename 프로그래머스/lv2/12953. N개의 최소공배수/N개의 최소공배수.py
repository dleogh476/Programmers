import math
def prime_num (n):
    p_num = list()
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i==j :
                p_num.append(i)
            elif (i%j)== 0:
                break      
    return p_num

def lcm(a,b):
    return a * b // math.gcd(a, b)

def solution(arr):
    answer = arr[0]
    
    for num in range(1,len(arr)):
        answer = lcm(answer,arr[num])
        
    return answer

