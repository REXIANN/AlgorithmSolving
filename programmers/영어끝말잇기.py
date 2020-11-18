def solution(n, words):
    tail = words[0][0]
    idx, time = 1, 1
    word_set = set()
    for word in words:
        if word[0] == tail:
            if word in word_set:
                return [idx, time]
            else:
                word_set.add(word)
                tail = word[-1]
        else:
            return [idx, time]
        idx += 1
        if idx > n:
            idx = 1
            time += 1
    
    return [0, 0]