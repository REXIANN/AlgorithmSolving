# 사다리 타기
import pprint
import sys
sys.stdin = open("1211input.txt", "r")

tc = 10

for test_count in range(1, tc + 1):
    input_ = int(input())
    print('#{}'.format(test_count), end=" ")

    matrix = []
    for i in range(100):
        matrix.append(list(map(int, input().split())))
    ## 제대로 들어갔음
    starting_array = []
    ending_array = []
    result = 1000000
    final_column = -1

    dr = [0, 1, 0]
    dc = [-1, 0, 1]



    def down(row, col):
        if matrix[row + dr[1]][col + dr[1]] == 1:
            return True
        else:
            return False


    # 1.첫번째 줄을 검사하여 시작지점을 찾아 인덱스를 저장하느 배열 만들기
    for idx, value in enumerate(matrix[0]):
        if value == 1: starting_array.append(idx)
    # print(starting_array)
    # [0, 3, 12, 18, 20, 31, 37, 47, 57, 61, 67, 74, 81, 84, 93, 96, 99]


    # 2.해당시작지점마다 출발해서 움직임을 카운트하며 내려감
    # 좌우에 1이 있으면 좌우이동, 없거나 0이면 하단이동
    for start_column in starting_array:
        row, column = 0, start_column
        count = 0


        while True:
            if column + dc[0] > -1 and matrix[row + dr[0]][column + dc[0]] == 1:

                while column + dc[0] > -1 and matrix[row + dr[0]][column + dc[0]] == 1:
                    row = row + dr[0]
                    column = column + dc[0]
                    count +=1

                row = row + dr[1]
                column = column + dc[1]
                count += 1
                #print('왼쪽이동')
                continue

            if column + dc[2] < 100 and matrix[row + dr[2]][column + dc[2]] == 1:

                while column + dc[2] < 100 and matrix[row + dr[2]][column + dc[2]] == 1:
                    row = row + dr[2]
                    column = column + dc[2]
                    count += 1

                row = row + dr[1]
                column = column + dc[1]
                count += 1
                #print('오른쪽이동')
                continue

            if row + 1 == 100:
                break

            row = row + dr[1]
            column = column + dc[1]
            count += 1
            #print('하강')
            if row + 1 == 100:
                break

        # 3.움직인 카운트를 새로운 배열에 저장
        # 해당 배열의 길이는 시작 인덱스 배열의 길이와 동일
        if count <= result:
            final_column = start_column
            result = count
    print(final_column)
    # 4.카운트배열의 제일 큰값을 가지는 뒤쪽 인덱스를 출력


