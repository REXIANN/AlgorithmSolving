import heapq

max_length = 1
h = []
def bt(k, cookies, length, arr):
    global max_length, h
    if length > max_length:
        max_length = length
        h = [arr]
    elif length == max_length:
        h.append(arr)
    for i in range(k + 1, len(cookies)):
        if cookies[i] > arr[-1]:
            sec_arr = arr + [cookies[i]]
            bt(i, cookies, length + 1, sec_arr)

                
def solution(cookies,k):
    for i in range(len(cookies) - 1):
        bt(i, cookies, 1, [cookies[i]]) 

    print(h)
    if k >= len(h) // 2:
        x = heapq.nlargest(len(h) - k + 1, h)
    else:
        x = heapq.nsmallest(k, h)
    return x[-1]
    

cookies = [1,4,2,6,5,3]
k = 2
print(solution(cookies, k))