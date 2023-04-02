def DFS(idx,computers,visit_list):
    if visit_list[idx] == True:
        return 1
    visit_list[idx] = True
    for i, num in enumerate(computers[idx]):
        if num == 1:
            DFS(i,computers, visit_list)
    #DFS(,computers, visit_list)
    return 1;

def solution(n, computers):            
    answer = 0
    visit_list = list()
    for idx in range(n):
        visit_list.append(False)
    #print(visit_list);
    
    for idx,isvisit in enumerate(visit_list):
        if isvisit:
            continue
        else :
            DFS(idx, computers, visit_list)
        answer += 1
    return answer