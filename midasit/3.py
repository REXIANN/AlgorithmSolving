import heapq

max_length = 1
def bt(k, cookies, length, value):
    global max_length
    if length > max_length:
        max_length = length
    for i in range(k + 1, len(cookies)):
        if cookies[i] > value:
            bt(i, cookies, length + 1, cookies[i])


h = []
def longest(k, length, cookies, arr):   
    if length == 0:
        h.append(arr)
    else:
        for i in range(k + 1, len(cookies)):
            if cookies[i] > arr[-1]:
                if len(cookies) - i < length:
                    return
                sec_arr = arr + [cookies[i]]
                longest(i, length - 1, cookies, sec_arr)   

                
def solution(cookies,k):
    for i in range(len(cookies) - 1):
        bt(i, cookies, 1, cookies[i])
        
    for i in range(len(cookies)):
        longest(i, max_length - 1, cookies, [cookies[i]])

    x = heapq.nlargest(len(h) - k + 1, h) if k >= len(h) // 2 else heapq.nsmallest(k, h)
    return x[-1]