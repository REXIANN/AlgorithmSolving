def left_sorting(matrix):
    #두개씩 비교해가면서 같으면 곱하고 0을 추가
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(j+1, len(matrix[i])):
                if matrix[i][k] == 0:
                    continue

                if matrix[i][k] == matrix[i][j]:
                    matrix[i][j] *= 2
                    matrix[i][k] = 0
                    break
                else:
                    break
    #0을 뒤로 보내는 연산
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            if matrix[i][j] != 0:
                continue

            for k in range(j+1, len(matrix[i])):
                if matrix[i][k] != 0:
                    matrix[i][j] = matrix[i][k]
                    matrix[i][k] = 0
                    break
    return matrix


def rotate(matrix):
    N = len(matrix)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = matrix[r][c]

    return ret


tc = int(input())

for test_count in range(1, tc + 1):
    print('#{}'.format(test_count))
    N_, S_ = input().split()
    matrix = []
    for _ in range(int(N_)):
        matrix.append(list(map(int, input().split())))
    #성공적으로 입력된 행렬
    #pprint.pprint(matrix); print()
    
    #정렬을 위해 왼쪽 정렬이 가능하게 돌림
    if S_ == 'right':
        matrix = rotate(rotate(matrix))
    elif S_ == 'up':
        matrix = rotate(matrix)
    elif S_ == 'down':
        matrix = rotate(rotate(rotate(matrix)))
    #pprint.pprint(matrix); print()
    
    #왼쪽정렬 끝냄
    matrix = left_sorting(matrix)
    #pprint.pprint(matrix); print()


    #다시돌림
    #pprint.pprint(matrix); print()
    if S_ == 'right':
        matrix = rotate(rotate(matrix))
    elif S_ == 'down':
        matrix = rotate(matrix)
    elif S_ == 'up':
        matrix = rotate(rotate(rotate(matrix)))
    
    for array in matrix:
        for value in array:
            print(value, end=" ")
        print()