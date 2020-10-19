def solution(number, k):
    num_list = []
    
    for i in range(len(number)):
        while num_list and k > 0 and num_list[-1] < number[i]:
            num_list.pop()
            k -= 1
        num_list.append(number[i])
    return ''.join(num_list)


number = '4177252841'
k = 4
print(solution(number, k))


#    ''.join(st[:len(st) - k])
