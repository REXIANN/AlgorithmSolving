import sys
sys.stdin = open('testinput.txt', 'r')

for t_count in range(1, 11):
    input()
    matrix = list(map(''.join, zip(*[input().replace(' ', '') for _ in range(100)])))

    for i in range(100):
        matrix[i] = matrix[i].replace('0', '').rstrip('01').lstrip('02')

    count = 0
    for i in range(100):
        for k in range(len(matrix[i]) - 1):
            if matrix[i][k:k + 2] == '12':
                count += 1
    print('#{} {}'.format(t_count, count))