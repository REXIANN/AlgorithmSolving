def solution(N, number):
    answer = [set([N])]
    for i in range(1, 8):
        arr = set()
        arr.add(sum([N * 10 ** j for j in range(i + 1)]))
        for s in answer[i - 1]:
            arr.add(s + N)
            arr.add(s - N)
            arr.add(s * N)
            arr.add(s // N)
        print(arr)   
        if number in arr:
            return i + 1
        else:
            answer.append(arr)
        
    return -1


N, number = 5, 12
print(solution(N, number))