# 1221.py GNS

import sys
sys.stdin = open("1221input.txt", "r")

# 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

tc = int(input())

for test_count in range(1, tc + 1):
    print('#' + str(test_count))
    number, length = input().split()
    input_string = input()
    #print(input_string)

    num_list = [0] * 10
    word_list = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
    for idx in range(int(length)):
        word = input_string[4 * idx]
        #print(word ,end="")
        if word == 'Z':
            num_list[0] += 1
        elif word == 'O':
            num_list[1] += 1
        elif word == 'T':
            if input_string[4 * idx + 1] == 'W':
                num_list[2] += 1
            else:
                num_list[3] += 1
        elif word == 'F':
            if input_string[4 * idx + 1] == 'O':
                num_list[4] += 1
            else:
                num_list[5] += 1
        elif word == 'S':
            if input_string[4 * idx + 1] == 'I':
                num_list[6] += 1
            else:
                num_list[7] += 1
        elif word == 'E':
            num_list[8] += 1
        elif word == 'N':
            num_list[9] += 1
    #print(num_list)
    for idx, number in enumerate(num_list):
        print((word_list[idx] * number).rstrip())

