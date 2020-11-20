# def solution(land):
#     answer = []
#     max_value = max(land[0])
#     max_index = land[0].index(max_value)
#     second_max = max([land[0][i] for i in range(len(land[0])) if i != max_index])
#     second_index = land[0].index(second_max)
#     answer.append((max_index, max_value, second_index, second_max))    
    
#     for i in range(1, len(land)):
#         mi, mv, si, sv = answer[i - 1]
#         mvv = max([land[i][j] for j in range(len(land[i])) if j != mi])
#         mii = land[i].index(mvv)
#         svv = max([land[i][j] for j in range(len(land[i])) if j != si])
#         sii = land[i].index(svv)
#         answer.append((mii, mv + mvv,  sii, sv + svv))

#     return max(answer[-1][1], answer[-1][3])


def solution(land):
    answer = []
    print(answer)
    
    for i in range(1, len(land)):
        arr = []
        for j in range(4):
            val = answer[i - 1][j]
            max_val = max([land[i][k] for k in range(4) if k != j])
            arr.append(val + max_val)
        answer.append(arr)
    return answer

land = [[1,2,3,5],[5,6,7,100],[4,3,2,1]]
print(solution(land))