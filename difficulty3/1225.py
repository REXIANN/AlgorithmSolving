# 1225.py 암호생성기

import sys
sys.stdin = open("1225input.txt", "r")
tc = 10 # int(input())

for test_count in range(1, tc + 1):
    print('#{} '.format(test_count), end="")
    number = int(input())
    numbers = list(map(int, input().split()))

    idx = 0
    count = 1

    while True:
        # 1씩 count를 증가시키면서 원래 수에서 빼줌
        numbers[idx] -= count
        
        # 만약 해당 숫자가 0보다 작으면 0으로 바꾸고 while문 탈출
        if numbers[idx] <= 0:
            numbers[idx] = 0
            break

        # count와 idx를 증가시키면서 진행
        # 만약 idx를 증가한 값이 8이라면 다시 0으로 만들어줌
        count +=1
        if count == 6:
            count = 1
        idx += 1
        if idx == 8:
            idx = 0
    
    numbers *= 2
    #print(numbers[idx + 1 : idx + 9].split())
    for i in range(1, 9):
        print(numbers[idx +i], end=" ")
    print()