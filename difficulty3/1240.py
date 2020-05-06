# 1240.py 단순2진 암호코드

for tc in range(int(input())):
    a_ = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    N_, M_ = map(int, input().split())
    matrix = [input() for _ in range(N_)]
    numbers = []
    row, col = -1, -1
    for i in range (0, N_, 5):
        for j in range(M_ - 1, M_ - 56, -1):
            if matrix[i][j] == '1':
                col = j; break; 
        if col != -1:
            row = i; break;   

    for i in range(8):
        numbers.append(a_.index(matrix[row][col - i * 7 - 6: col - i * 7 + 1]))  

    result = sum(numbers[::2]) + 3 * sum(numbers[1::2])
    final = sum(numbers) if result % 10 == 0 else 0
    print('#{} {}'.format(tc + 1, final))
