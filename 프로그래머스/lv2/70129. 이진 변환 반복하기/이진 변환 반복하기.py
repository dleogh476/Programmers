def solution(s):
    answer = []
    loop_count = 0
    remove_zero_count = 0
    
    while True:
        #loop count
        loop_count = loop_count + 1
        #split s
        s_list = list(s)

        #zero remove
        for num in range(len(s_list)):  
            if s_list[num] == '0':
                remove_zero_count = remove_zero_count + 1 
        s = s.replace('0','')        
        # '1' count
        new_s = bin(len(s))
        new_s = new_s.replace('0b','')
        s = str(new_s)
        

        #stop s == '1'
        if s == '1':
            answer.append(loop_count)
            answer.append(remove_zero_count)
            return answer
    