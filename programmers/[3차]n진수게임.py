def solution(n, t, m, p):
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    memory = []
    for i in range(p + t * m):
        if i == 0:
            memory.append(i)
        
        stack = []
        while i != 0:
            val = i % n
            if hex_dict.get(val):
                stack.append(hex_dict[val])
            else:
                stack.append(val)
            i = i // n
        
        while stack:
            value = stack.pop()
            memory.append(value)
      
    answer = []
    idx = p - 1
    while t > 0:
        answer.append(str(memory[idx]))
        idx += m
        t -= 1
    return ''.join(answer)