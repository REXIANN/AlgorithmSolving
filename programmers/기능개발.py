from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque(progresses)
    while dq:
        for i in range(len(dq)):
            dq[i] += speeds[i]
            if dq[i] > 100:
                dq[i] = 100
                
        count = 0
        while dq and dq[0] == 100:
            count += 1
            value = dq.popleft()
        
        if count != 0:
            answer.append(count)
            count = 0
       
    return answer

progresses = [93, 30, 55]	
speeds = [1, 30, 5]
print(solution(progresses, speeds))