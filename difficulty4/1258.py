# 1258.py 행렬찾기
import pprint
import sys

sys.stdin = open("1258input.txt", "r")

# 그룹 1. n <= 10 이고 sub matrix의 개수 5개 이하
# 그룹 2. n <= 40 이고 5 < sub matrix <= 10
# 그룹 3. 40 < n <=80 이고 5 < sub matrix <= 10
# 그룹 4. 40 < n <=80 이고 10 < sub matrix <= 15
# 그룹 5. 80 < n<=100 이고 15 < sub matrix <= 20


tc = int(input())

for test_count in range(1, tc + 1):
    N_ = int(input())
    matrix = [[0] * (N_ + 2)]
    matrix.extend([[0] + list(map(int, input().split())) + [0] for _ in range(N_)])
    matrix.append([0] * (N_ + 2))
    sub_matrix = set()
    sub_lists_sum = []
    
    dr = [0, 1]
    dc = [1, 0]
    direction, i, j = 0, 1, 1

    for i in range(N_ + 1):

        for j in range(N_ + 1):

            if matrix[i][j] != 0:
                sub_row, sub_col = 0, 0
                row, col = i, j
                if matrix[row - 1][col] != 0 or matrix[row][col - 1] != 0:
                    continue

                while True:
                    sub_row += 1
                    row += dr[direction]
                    col += dc[direction]

                    if matrix[row][col] == 0:
                        row -= dr[direction]
                        col -= dc[direction]
                        direction = 1
                        break

                while True:
                    sub_col += 1
                    row += dr[direction]
                    col += dc[direction]

                    if matrix[row][col] == 0:
                        row -= dr[direction]
                        col -= dc[direction]
                        j = col
                        direction = 0
                        break

                sub_matrix.add((sub_col, sub_row))
    
    
    sub_lists = list(sub_matrix)
    for subs in sub_lists:
        sub_lists_sum.append(subs[0] * subs[1])
    #print('sub_lists:', sub_lists)
    
    for sub in subs:
        if subs.count(sub) >= 2:
            pass
    
    #print('sub_lists_sum:', sub_lists_sum)
    sub_lists_srtd = sub_lists_sum[:]
    sub_lists_srtd.sort()
    #print('sub_lists_srtd:', sub_lists_srtd)

    final_list = []
    for i in range(len(sub_lists)):
        final_list.append(sub_lists[sub_lists_sum.index(sub_lists_srtd[i])])
    #print('final_list:', final_list, '\n')

    value = -1
    control = False
    for val in sub_lists_sum:
        if sub_lists_sum.count(val) >= 2:
            value = val
            control = True
            break
    while control:
        indexing = []
        for idx, val in enumerate(sub_lists_sum):
            if val == value:
                indexing.append(idx)
        #print(indexing)
        if sub_lists[indexing[0]][0] >  sub_lists[indexing[1]][0]:
                asdf = sub_lists[indexing[0]][0] * sub_lists[indexing[0]][1]
                #print(asdf)
                indexxx = sub_lists_srtd.index(asdf)
                #print(indexxx)
                #print(final_list[indexxx], sub_lists[indexing[1]])
                final_list[indexxx] = sub_lists[indexing[1]]
        else:
            asdf = sub_lists[indexing[0]][0] * sub_lists[indexing[0]][1]
            #print(asdf)
            indexxx = sub_lists_srtd.index(asdf) + 1
            #print(indexxx)
            final_list[indexxx] = sub_lists[indexing[0]]
        break

    print('#{}'.format(test_count), end=" ")    
    #print('final_list:', final_list, '\n')
    for xxx in final_list:
        for xx in xxx:
            print(xx, end=" ")
    print()    