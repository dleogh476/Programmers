def solution(citations):
    citations.sort()
    for idx in range(len(citations)):
#citations[num] h 인용 회수, len(citations) - num h이상 인용된 논문수, num h이하 인용된 논문수
        if citations[idx] >= len(citations) - idx:
            #return citations[idx]
            return len(citations) - idx 
            
    return 0