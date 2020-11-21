def solution(land):
    answer = [[l for l in land[0]]]   
    for i in range(1, len(land)):
        answer.append([land[i][j] + max([answer[i - 1][k] for k in range(4) if k != j]) for j in range(4)])
    return max(answer[-1])

land = [[1,2,3,5],[5,6,7,100],[4,3,2,1]]
print(solution(land)) 