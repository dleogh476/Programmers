def solution(arr):
    answer = []
    
    fornt_num = arr[0]
    answer.append(fornt_num)
    
    for num_idx in range(1,len(arr)):
        if fornt_num != arr[num_idx]:
            answer.append(arr[num_idx])
            fornt_num = arr[num_idx]
    return answer