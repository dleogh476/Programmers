#import queue
def solution(progresses, speeds):
    answer = []
    day_count = 0
    #prog_queue = queue.Queue()
    while(True):
        #1. 남아있는 모든 요소에 speeds의 값을 더함
        for idx, prog in enumerate(progresses):
            progresses[idx] = speeds[idx] + prog
            #print(progresses)
    
        #2. 첫번째 요소가 100을 넘었는지 확인
        #3. 넘을 경우 progresses, speed 둘다 내보내고  
        #   뒤에 있는 요소들도 확인해서 100넘는 것들도 한번에 내보냄 
        for prog in progresses:
            if prog < 100:
                break
            day_count += 1
            
        for c in range(day_count):
            progresses.pop(0)
            speeds.pop(0)
        
        #print(progresses)
        #4. 내보낸 갯수를 answer에 저장
        if day_count > 0:
            answer.append(day_count)
            day_count = 0
            
        #5. 모든 progress가 끝나면 프로그램 종료
        if len(progresses) <= 0:
            return answer
    return answer