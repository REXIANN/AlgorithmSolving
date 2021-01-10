def solution(arr):   
    a = []
    key = '_'
    for ar in arr:
        if key != ar:
            a.append(ar)
            key = ar
        
    return a