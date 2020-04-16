def check(arr, arg):
    global checksum
    if len(arr) <= 2:
        if arg in arr: 
            checksum = 1
            return
    
    mid = len(arr) // 2
    if arr[mid] == arg: 
        checksum = 1
        return
    elif arr[mid] < arg: 
        check(arr[mid:], arg)
    else:
        check(arr[:mid], arg)

def solution(k, room_number):
    global checksum
    idx = 0
    check = [0] * (max(room_number) + 1)
    answer = []
    lgth = len(room_number)
    while idx < lgth:
        number = room_number[idx]
        # if len(check) - 1 < number:
        #     check[len(check):len(check)] = [0] * (number - len(check) + 1)

        # if number not in answer:
        check(answer.sort(), number)
        if checksum & 1:
            answer.append(number) 
            checksum = 0
            check[number] = 1
        else:
            while True:
                number += 1
                if len(check) == number:
                    answer.append(number)
                    check.append(1)
                    break

                if not check[number] & 1:
                    answer.append(number)
                    check[number] = 1
                    break
            
        idx += 1
    return answer
checksum = 0
print(check([1, 2, 3, 4, 5], 1))
print(solution(10, [1, 3, 4, 1, 3, 1]))