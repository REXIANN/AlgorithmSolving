def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            val = 0
            for k in range(len(arr1[0])):
                val += arr1[i][k] * arr2[k][j]
            answer[i].append(val)          
    return answer


def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            answer[i].append(sum([arr1[i][k] * arr2[k][j] for k in range(len(arr1[0]))]))          
    return answer


def solution(arr1, arr2):
    return [[sum([arr1[i][k] * arr2[k][j] for k in range(len(arr1[0]))]) for j in range(len(arr2[0]))] for i in range(len(arr1))]