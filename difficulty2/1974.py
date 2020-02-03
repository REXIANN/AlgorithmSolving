# 1974. 스도쿠 검증
import pprint
import sys
sys.stdin = open("1974input.txt", "r")
# 입력으로 9x9크기의 스도쿠퍼즐의 숫자들이 주어진다.
# 가로, 세로, 3x3 사각형안에 겹치는 숫자가 없을 경우 통과.
# 스도쿠가 완성될경우 1, 아닐 경우 0 을 출력한다.

tc = int(input())

for test_count in range(tc):
    sudoku = []
    result = 1
    sum_ = []
    cin = 0

    for i in range(9):
        sudoku.append(list(map(int, input().split())))
    # pprint.pprint(sudoku)
    
    for i in range(9):
        sum_row = sum([j for j in sudoku[i]])
        for j in range(9):
            cin += sudoku[j][i]
        sum_column = cin
        # print('SUM_ROW', sum_row,'SUM_COL', sum_column)
        
        if sum_row != 45 or sum_column != 45:
            result = 0
        cin = 0
    
    for i in range(3):      
        for j in range(3):
            for k in range(3):
                sum_.append( sum(sudoku[3 * i + k][3 * j : 3 * j + 3]))
        
            sum_sum = sum_[0] + sum_[1] + sum_[2]
            # print(sum_, sum_sum)
            
            if sum_sum != 45:
                sum_.clear()
                result = 0

            sum_.clear()

    sudoku.clear()      
    
    print('#{} {} '.format(test_count + 1, result))