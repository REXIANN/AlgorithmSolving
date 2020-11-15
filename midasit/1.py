def solution(openA, closeB):
    setA = set(openA)
    setB = set(closeB)
    is_open = False
    count = 0
    gap = 0
    for i in range(1, closeB[-1] + 1):
        if i in setA:
            if is_open:
                pass
            else:
                is_open = True
                gap = i
        if i in setB and is_open:
            is_open = False
            count += i - gap
            
    return count