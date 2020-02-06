# 1220.py Magnetic
import pprint
import sys
sys.stdin = open("1220input.txt", "r")

tc = 11
for t_count in range(1, tc):
    n_ = input()
    matrix = []
    lock_count = 0
    for i in range(100):
        matrix.append(input().replace(' ',''))
    
    # print(matrix)
    # ['1000000020001011020010202210000010020000012000110000200001000002000200000000010000000000100000000201', 
    #  '0000000000100200000200100000120010000100000000001020000001200000000120100001000010000000000000010000', 
    #  '0001000000000002000000000000000100002202000001000120200020000200102110002002000010100020200000220010',]

    matrix_zip = list(map(''.join, zip(*matrix)))
    #print(matrix_zip[0])
    
    for i in range(100):
        matrix_zip[i] = matrix_zip[i].replace('0', '')
        matrix_zip[i] = matrix_zip[i].rstrip('01').lstrip('02')
    #pprint.pprint(matrix_zip)
    
    for idx in range(100):
        for k in range(len(matrix_zip[idx])-1):
            if matrix_zip[idx][k:k+2] == '12':
                lock_count += 1
        #print(matrix_zip[idx])
    print('#{} {}'.format(t_count,lock_count))

                
