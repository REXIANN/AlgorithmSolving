def solution(a):
    answer = 0
    # 빈도수 가지는 배열 생성
    frequency = [[0, []] for _ in range(len(a) + 1)] 
    for idx, value in enumerate(a):
        frequency[value][0] += 1
        frequency[value][1].append(idx)
    print(frequency)
    
    # 각원소마다 그리디 사용(왼->오, 오->왼 두번 탐색)
    for freq in frequency:
        if freq[0] == 0:
            continue
        
        # arr배열을 freq[1]의 위치 양옆으로 탐색
        left_flag = False
        star_set = set()
        # 왼쪽
        for f in freq[1]:
            check = False
            if f - 1 > 0:
                if a[f - 1] != freq[0]:
                    if f - 1 not in start_set:
                        star_set.add(f - 1)
                    else:
                        break
            elif f + 1 < len(a):
                if a[f + 1] != freq[0]:
                    if f + 1 not in start_set:
                        star_set.add(f + 1)
                    else:
                        break
            else:
                break
        else:
            answer = freq[0] * 2 if freq[0] * 2 > answer else answer
            left_flag = True 
        
        # 오른쪽. 왼쪽에서 통과하면 할필요 없음
        if left_flag:
            continue
        right_flage = False
        for f in freq[1]:
            check = False
            if f + 1 > len(arr):
                if not arr[f + 1]:
                    arr[f + 1] = True
                    check = True
            elif f - 1 < 0:
                if not arr[f - 1]:
                    arr[f - 1] = True
                    check = True
            
            if not check:
                break
        else:
            right_flage = True
        
        if right_flage:
            answer = freq[0] * 2 if freq[0] * 2 > answer else answer
    
    return answer

a = [5,2,3,3,5,3]
print(solution(a))