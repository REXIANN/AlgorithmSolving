  
def solution(N, number):
    answer = -1
    temp = [set() for _ in range(9)]
    for i in range(1, 9):
        temp[i].add(int(str(N)*i))
    for i in range(1, 9):
        for j in range(i):
            for num1 in temp[j]:
                for num2 in temp[i-j]:
                    temp[i].add(num1+num2)
                    temp[i].add(num1-num2)
                    temp[i].add(num1*num2)
                    if num2 != 0:
                        temp[i].add(num1//num2)
        print(len(temp[i]), 'start', sorted(list(temp[i])))
        print()
        if number in temp[i]:
            answer = i
            break
    return answer

print(solution(5, 12))