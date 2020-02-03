# 1979.py

import sys
sys.stdin = open("1979input.txt", "r")

# NxN 크기의 단어퍼즐을 만듬. 입력으로 단어퍼즐의 모양이 주어진다.
# 주어진 퍼즐모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
# 길이K는 정확하게 공백의 길이와 일치해야 한다.
# 5 <= N <= 15, 2 <= K <= N
#  

tc = int(input())

for test_count in range(1, tc+1):
    N_, K_ = tuple(map(int,(input().split())))
    puzzle = []
    for _ in range(N_):
        puzzle.append(list(map(int, input().split())))
    # print(N_, K_, type(N_), type(K_))
    # 5 3 <class 'int'> <class 'int'>
    # print(puzzle)
    # [[0, 0, 1, 1, 1], [1, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
    # 흰색부분은 1, 검은색 부분은 0 (흰색에 단어가 들어간다)

    count = 0
    test_string ='0' + '1' * K_ + '0'
    test_string_for_the_start = '1' * K_ + '0'
    test_string_for_the_end = '0' + '1' * K_
    print('test string: {}  (start: {}, end: {})'.format(test_string, test_string_for_the_start, test_string_for_the_end))

    # search for each row
    print('#{}th row'.format(test_count))
    for h in range(N_):
        for i in range(N_ - K_ -1):
            blanks = ''
            for j in range(i, i + K_ + 2):
                blanks += '1' if puzzle[h][j] == 1 else '0'
            
            if blanks == test_string:
                count += 1

            if i == 0:
                if blanks[:i + K_ + 1] == test_string_for_the_start:
                    count += 1
            
            if i == (N_ - K_ - 2):
                if blanks[1:] == test_string_for_the_end:
                    count += 1
            
        #     print(blanks, end=' ')
        # print('\n {}'.format(count))


    
    print('#{}th column'.format(test_count))
    # search for each column
    for h in range(N_):
        for i in range(N_ - K_ -1):
            blanks = ''
            for j in range(i, i + K_ + 2):
                blanks += '1' if puzzle[j][h] == 1 else '0'
            
            if blanks == test_string:
                count += 1
            
            if i == 0:
                if blanks[:i + K_ + 1] == test_string_for_the_start:
                    count += 1

            if i == (N_ - K_ - 2):
                if blanks[1:] == test_string_for_the_end:
                    count += 1
        #     print(blanks, end=' ')
        # print('\n {}'.format(count))

    print(count)