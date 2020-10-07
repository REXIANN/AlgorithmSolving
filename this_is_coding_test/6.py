# 6. 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891 
def solution(food_times, k):
    answer = 0
    if k >= sum(food_times): 
        return -1

    while k > len(food_times):
        gap = k // len(food_times)
        for i in range(len(food_times)):
            if food_times[i] == 0:
                continue
            elif food_times[i] >= gap:
                food_times[i] -= gap
                k -= gap
            elif 0 < food_times[i] < gap:
                k -= food_times[i]
                food_times[i] = 0
    print('#1', food_times, k)
    
    idx = 0
    while k > 0:
        if food_times[idx] > 0:
            food_times[idx] -= 1
            k -= 1      
        idx += 1
        if idx == len(food_times):
            idx = 0
    print('#2', food_times, k)

    while True:
        if food_times[idx] > 0:
            answer = idx
            break
        idx += 1
        if idx == len(food_times):
            idx = 0
    print('#3', food_times, k)

    return answer + 1


k = 1000000000
food_times = [500000000, 1, 1, 1, 500000000, 1, 1, 1, 1, 1]

print(solution(food_times, k))
