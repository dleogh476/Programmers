import heapq
def solution(n, works):
    answer = 0
    maxheap_works = []
    num = 0 
    for w in works:
        num += w
    if num <= n :
        return 0
    
    #minheap
    #heapq.heapify(works)
    
    #maxheap
    for w in works:
        heapq.heappush(maxheap_works, (-w, w))
    print(maxheap_works)
    
    while n != 0:
        i = heapq.heappop(maxheap_works)
        num = i[1] - 1
        i = (-num, num)
        n -= 1
        heapq.heappush(maxheap_works,i)
    
    for num in maxheap_works:
        answer += num[1]**2
    return answer