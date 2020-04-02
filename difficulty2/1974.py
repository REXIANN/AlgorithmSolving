# 1974. 스도쿠 검증
from pprint import pprint
import sys
sys.stdin = open("1974input.txt", "r")
# 파이썬 배운지 1달 됐을 때 짠 코드
def f(M):
    for i in range(9):
        S = set(M[i])
        if len(S) != 9: return 0
    return 1 

def ff(M):
    for i in range(0, 9, 3): # row
        for j in range(0, 9, 3): # column
            S = set(M[i+k][j+m] for m in range(3) for k in range(3))
            if len(S) != 9: return 0
    return 1

for tc in range(int(input())):
    M = [list(map(int, input().split())) for _ in range(9)]
    MM = list(map(list, zip(*M)))
    print('#{} {}'.format(tc+1, f(M)*f(MM)*ff(M)))
    













# 파이썬 배운지 1주일 됐을 때 짠 코드
# tc = int(input())

# for test_count in range(tc):
#     sudoku = []
#     result = 1
#     sum_ = []
#     cin = 0

#     for i in range(9):
#         sudoku.append(list(map(int, input().split())))
#     # pprint.pprint(sudoku)
    
#     for i in range(9):
#         sum_row = sum([j for j in sudoku[i]])
#         for j in range(9):
#             cin += sudoku[j][i]
#         sum_column = cin
#         # print('SUM_ROW', sum_row,'SUM_COL', sum_column)
        
#         if sum_row != 45 or sum_column != 45:
#             result = 0
#         cin = 0
    
#     for i in range(3):      
#         for j in range(3):
#             for k in range(3):
#                 sum_.append( sum(sudoku[3 * i + k][3 * j : 3 * j + 3]))
        
#             sum_sum = sum_[0] + sum_[1] + sum_[2]
#             # print(sum_, sum_sum)
            
#             if sum_sum != 45:
#                 sum_.clear()
#                 result = 0

#             sum_.clear()

#     sudoku.clear()      
    
#     print('#{} {} '.format(test_count + 1, result))