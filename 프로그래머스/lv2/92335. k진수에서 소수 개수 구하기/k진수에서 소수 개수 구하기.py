def primenumber(x):
    if x ==1 :
        return False
    for i in range(2, int(x**(1/2))+ 1):	
    	if x % i == 0:		
        	return False
    return True	

def solution(n, k):
    answer = 0
    num_str = list()
    number = ""
    numbers = list()

    while n != 0:
        a = n % k
        n = n//k
        num_str.append(str(a))
    for stra in num_str:
        number = stra + number
    
    numbers = number.split('0')
    
    for i in numbers:
        if i == '':
            continue
        b = int(i)
        if primenumber(b):
            #print(b)
            answer += 1
            
            
    return answer