def solution(n, words):
    answer = [0,0]
    word_dict = dict()
    
    for word in words:
        word_dict[word] = False 
    word_dict[words[0]] = True    
    for count in range(1,len(words)):    
        if word_dict[words[count]] or words[count][0] != words[count-1][-1]:
            answer[0] = (count % n) + 1 
            answer[1] = (count // n) + 1
            return answer
        word_dict[words[count]] = True

    return answer