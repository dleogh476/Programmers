def solution(s):
    answer = ''
    list_of_string = s.split(" ")
    answer_list = list()
    for str1 in list_of_string:
        
        
        # chr -> int(ascii)            
        if '' == str1 :        
            answer_list.append('')
        else :
            str1 = str1.lower()
            frist_ascii =  ord(str1[0])
            
            if frist_ascii >= 97 and frist_ascii <= 122:  
                frist_ascii = frist_ascii - 32            
                # int(ascii) -> chr , chr in str
                l = list(str1)
                l[0] = chr(frist_ascii)
                str1 = ''.join(l)

            answer_list.append(str1)
        
        answer = ' '.join(answer_list)
        
    return answer