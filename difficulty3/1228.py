# 1228.py 암호문1
import pprint
import sys
sys.stdin = open("1228input.txt", "r")


tc = 10
for test_count in range(1, tc + 1):
    N_ = int(input()) # 원본 암호문의 길이 10 ≤ N ≤ 20
    string = list(map(int, input().split()))[:10] # 원본 암호문
    M_ = int(input()) # 명령어 개수 5 ≤ N ≤ 10
    commands = list(input().split()) # 명령어들
    # pprint.pprint(string)
    # print(commands)
    index = 0

    while index < len(commands):
        # if commands[index] == 'I':
        location, count = int(commands[index + 1]), int(commands[index + 2])
        index += 3
        if location >= 10:
            index = index + count
            continue

        if location + count >= 10:
            temp_index = index
            for i in range(location, 10):
                string[i] = int(commands[index])
                index += 1
            index = temp_index + count
        
        elif location + count < 10:
            for i in range(10 - count -1, location - 1, -1 ):
                string[i + count] = string[i]

            for i in range(location, location + count):
                string[i] = int(commands[index])
                index += 1
                
    print('#{}'.format(test_count), end=" ")
    for num in string:
        print(num, end=" ")   
    print()         
