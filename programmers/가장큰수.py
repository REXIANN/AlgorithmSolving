def solution(numbers):
    numbers = sorted(map(str, numbers), reverse=True)
    orders = [[] for _ in range(10)]
    for number in numbers:
        orders[int(number[0])].append(number)
    
    
    for i in range(len(orders)):
        orders[i].sort(key = lambda x: x[0] if len(x) == 1 else x[0] if x[1] < x[0] and len(x) == 2 else x[1], reverse = True)
    
    # print(orders)
    result = []
    for i in range(9, -1, -1):
        result.append(''.join(orders[i]))
        
    return ''.join(result)

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
