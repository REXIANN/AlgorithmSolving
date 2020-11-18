def solution(s):
    min_length = len(s)
    for i in range(1, len(s) // 2 + 1):
        length = len(s)
        prev = s[:i]
        idx = 0
        flag = False
        count = 0
        while idx + i <= len(s):
            idx += i
            now = s[idx:idx + i]
            if prev == now:
                length -= len(now)
                flag = True
                count += 1

            if prev != now:
                if flag:
                    length += 1
                    flag = False
                    count = 0
            print(idx, prev, now, length)
            prev = now
        
        if flag:
            length += 1
        if length < min_length:
            min_length = length
                    
    return min_length


s = 'aabbaccc'
print(solution(s))