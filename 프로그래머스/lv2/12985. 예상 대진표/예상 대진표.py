import math

def solution(n,a,b):

        
    for win in range(1,21):   
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        if a == b :             
            return win
        
