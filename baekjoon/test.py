row, col = 3, 4
D = 5




for i in range(1, 2 * D, 2):
    for j in range(-(i//2), i//2 + 1, 1):
        row_in, col_in = (row + 1 + i//2 - abs(j)), (col + j)
        if is_end(row_in, col_in) and matrix[row_in][col_in] == 1:
            print(row_in, col_in)
            matrix[row_in][col_in] += 1
            flag = 1
            break
    print()



def is_end(row, col):
    if (row + 1 + i//2 - abs(j)) < 0 or  (row + 1 + i//2 - abs(j)) >= N:
        return False
    if col + j < 0 or col + j >= M:
        return False
    return True 