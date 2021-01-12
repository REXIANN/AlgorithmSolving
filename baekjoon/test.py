# 19236.py 청소년상어
import sys
sys.stdin = open('19236input.txt', 'r')
from collections import deque
import copy

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

results, matrix = [], [] 

for i in range(4):
    li = list(map(int, input().split()))
    matrix.append([(li[j] - 1, li[j + 1] - 1) for j in range(0, 8, 2)])

# shark is set for 16
fish, direction = matrix[0][0]
matrix[0][0] = (16, direction)
shark_count = fish + 1

# put the matrix and shark count as a tuple into the deque
dq = deque([(matrix, shark_count)])

# TOSHOW -> FIRST STEP
# print('first shark', shark_count)
# for i in range(4):
#     print(matrix[i])
# print()

while dq: 
    # pop
    matrix, shark_count = dq.popleft()

    # fish move
    for k in range(16): # all fishes
        r_flag, c_flag = False, False
        for r in range(4):
            for c in range(4):
                if matrix[r][c][0] == k: # find appropriate fish
                    r_flag, c_flag = True, True
                    fish, direction = matrix[r][c] 
                    # print(k, r, c, direction)
                    # for i in range(4):
                    #     print(matrix[i])
                    # print()
                    for i in range(8):
                        # find available path for fish
                        i += direction
                        if i >= 8:
                            i -= 8
                        rr, cc = r + dr[i], c + dc[i]
                        if 0 <= rr < 4 and 0 <= cc < 4 and matrix[rr][cc][0] != 16:
                                matrix[r][c] = matrix[rr][cc]
                                matrix[rr][cc] = (fish, i)
                                break
                if c_flag:
                    break
            if r_flag:
                break    
    
    # TOSHOW -> ARRANGED MATRIX
    # for i in range(4):
    #     print(matrix[i])
    # print()

    # find available shark moves and append its matrix into deque
    # don't forget to add the value shark_count into results 
    sr, sc, s_dir = [(r, c, matrix[r][c][1]) for r in range(4) for c in range(4) if matrix[r][c][0] == 16][0]
    for i in range(1, 4):
        shark_inner_count = shark_count
        srr, scc = sr + dr[s_dir] * i, sc + dc[s_dir] * i
        if 0 <= srr < 4 and 0 <= scc < 4:
            if matrix[srr][scc][0] < 16:
                fish, direction = matrix[srr][scc]
                inner_matrix = copy.deepcopy(matrix)
                inner_matrix[sr][sc] = (20, 20)
                inner_matrix[srr][scc] = (16, direction)
                shark_inner_count += (fish + 1)
                # TOSHOW -> AVAILABLE SHARK PATHS
                # print('shark inner count', shark_inner_count)
                # for i in range(4):
                #     print(inner_matrix[i])
                # print()
                dq.append((inner_matrix, shark_inner_count))
                results.append(shark_inner_count)
    # print(dq)

# print('final result here')
# print('results', results)
print(max(results))
