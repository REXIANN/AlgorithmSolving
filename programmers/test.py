def solution(n, arr1, arr2):
    m1 = ['{:0{}b}'.format(ar1, n) for ar1 in arr1]
    m2 = ['{:0{}b}'.format(ar2, n) for ar2 in arr2]
    print(m1)
    print(m2)
    answer = [ ''.join(['#' if m1[i][j] == '1' or m2[i][j] == '1' else ' ' for j in range(n)]) for i in range(n)]
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))