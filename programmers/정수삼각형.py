def solution(triangle):
    answer = [triangle[0]]
    for i in range(1, len(triangle)):
        arr = []
        for j in range(len(triangle[i])):
            flag = False
            if j == 0:
                arr.append(triangle[i][j] + answer[i - 1][j])
            elif j == len(triangle[i - 1]):
                arr.append(triangle[i][j] + answer[i - 1][j - 1])    
            else:
                arr.append(triangle[i][j] + max(answer[i - 1][j - 1], answer[i - 1][j]))                
        answer.append(arr)
        
    return max(answer[-1])