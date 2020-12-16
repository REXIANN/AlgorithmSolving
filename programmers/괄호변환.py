def solution(p):
    answer = ''
    if not len(p): 
        return answer
    
    selector = 0
    p_idx = 0
    for pp in p:
        if pp == '(':
            selector += 1
        else:
            selector -= 1
        p_idx += 1
        if not selector:
            break
    
    u, v = p[:p_idx], p[p_idx:]
    print(u, v)
    isGood = True
    flag = 0
    for uu in u:
        if uu == '(':
            flag += 1
        else: 
            flag -= 1
        
        if flag < 0:
            isGood = False
            break

    if isGood:
        answer = u + solution(v)
    else:
        answer = '('
        answer = answer + solution(v) + ')'

        u_new = ''
        if len(u) <=  2:
            pass
        else:
            u_new = ''.join([')' if u[i] == '(' else '(' for i in range(1, len(u) -1)])
            # print(u_new)
        answer += u_new

    return answer