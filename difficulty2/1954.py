# 1954.py 달팽이 숫자

import pprint
import sys
sys.stdin = open("1954input.txt", "r")

# 달팽이의 크기 N은 1이상 10이하의 정수이다. (N= 1~ 10)

# 1 2 3
# 8 9 4
# 7 6 5

#  1  2  3  4
# 12 13 14  5
# 11 16 15  6
# 10  9  8  7



tc = int(input())

for test_count in range(tc):
    print('#{}'.format(test_count + 1))
    rect_size = int(input())
    rect = [[0 for _ in range(5)] for _ in range(5)]
    number = 1
    dir = 0
  
    # pprint.pprint(rect)
    
    def is_wall(x, y, array):
        if x <=0 or x > rect_size:
            return True
        if y <= 0 or y > rect_size:
            return True
        if rect[x][y] != 0:
            return True
        return False

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(rect_size):
        rect[0][i] = number
        number += 1
    
    rect_size -= 1
    dir += 1
    pprint.pprint(rect)
    ##########  #############

    while rect_size > 0:
        if dir >= 4:
            dir %= 4
        
        #common_index = 0
        #아래로
        
        for i in range(rect_size):
            idx_x = x + dx[i]
            idx_y = y + dx[i]
            if is_wall(idx_x, idx_y, rect) == True:
                rect[idx_x][idx_y] = number
                number += 1
            if is_wall(idx_x, idx_y, rect) == False:
                number += 1
                dir += 1
                break

        #왼쪽으로
        for i in range(rect_size, -1, -1):
            rect[rect_size][i] = number
            number += 1

        #인덱스 -1 해주기
        rect_size -= 1

        #인덱스가 0보다 작다면 브레이크
        if rect_size == 0:
            break
        
        #위로
        for i in range(rect_size, -1, -1):
            rect[i][i] = number
            number += 1

        #오른쪽으로
        for i in range(rect_size):
            rect[0][i] = number
            number += 1
        
        #인덱스 -1 해주기
        rect_size -= 1


# 기존에 NxN배열에 1~N까지의 숫자가 무작위로 들어있다고 가정할때
# 그 배열에서 작은숫자들을 순서대로 빼내는 함수
def sel_min():
    min_x, min_y = 0, 0
    for i in range(5):
        for j in range(5):
            if rect[min_x][min_y] > rect[i][j]:
                min_x, min_y = i, j
    min = rect[min_x][min_y]
    rect[min_x][min_y] = 99
    return min

    

X, Y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir_stat = 0 # 0:오른쪽 1:아래 2:왼쪽 3:위

for i in range(25):
    cur_min = sel_min()
    rect[X][Y] = cur_min
    X += dx[dir_stat]
    Y += dy[dir_stat]

    if is_wall(X, Y):
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = (dir_stat + 1) % 4
        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]
        
