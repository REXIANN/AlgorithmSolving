# 1230.py 암호문3
import sys
sys.stdin = open("1230input.txt", "r")


tc = 10
for test_count in range(1, tc + 1):
    N_ = int(input()) # 원본 암호문의 길이 100 ≤ N ≤ 200
    string = list(map(int, input().split())) # 원본 암호문
    M_ = int(input()) # 명령어 개수 10 ≤ N ≤ 20
    commands = list(input().split()) # 명령어들
    # pprint.pprint(string)
    # print(commands)
    index = 0

    while index < len(commands):
        
        if commands[index] == 'A':
            count = int(commands[index + 1])
            index = index + 2 + count
            continue

        if commands[index] == 'I':
            location, count = int(commands[index + 1]), int(commands[index + 2])
            index += 3

            for i in range(N_ - count -1, location - 1, -1 ):
                string[i + count] = string[i]

            temp = index    
            if location + count >= N_:
                for i in range(location, N_):
                    string[i] = int(commands[index])
                    index += 1
                index = temp + count
            else:
                for i in range(location, location + count):
                    string[i] = int(commands[index])
                    index += 1

        elif commands[index] == 'D':
            location, count = int(commands[index + 1]), int(commands[index + 2])

            for i in range(location, N_ - count):
                string[i] = string[i + count]
            index += 3

    print('#{}'.format(test_count), end=" ")
    for i in range(10):
        print(string[i], end=" ") 
    print()  