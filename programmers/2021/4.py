

def solution(n, s, a, b, fares):
    answer = 0
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    matrix_a = [[0] * (n + 1) for _ in range(n + 1)]
    matrix_b = [[0] * (n + 1) for _ in range(n + 1)]

   for fare in fares:
        r, c, m = fare[0], fare[1], fare[2]
        matrix[r][c] = m
        matrix[c][r] = m

    
    for i in range(n):
        print(matrix[i])

    return answer


def graph(a, s):
    pass


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, s, a, b, fares)
