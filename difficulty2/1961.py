# 1961. 숫자 배열 회전

import pprint
import sys
sys.stdin = open("1961input.txt", "r")

# NxN행렬이 주어질때 시계방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
# N은 3이상 7이하이다.
# 입력과는 달리 회전한 모양사이에만 공백이 존재함에 유의하라

# 원본행렬
# 1 2 3
# 4 5 6
# 7 8 9

# 회전한 행렬 세개
# 741 987 369
# 852 654 258
# 963 321 147

tc = int(input())

for test_count in range(tc):
    length = int(input())
    rectangle = []
    for _ in range(length):
        rectangle.append(list(map(int, input().split())))

    # pprint.pprint(rectangle)
    print('#{}'.format(test_count + 1))
    for i in range(length):
        for j in range(length):
            print(rectangle[(length-1)-j][i],end="")
        print(end=" ")
        for j in range(length):
            print(rectangle[(length-1)-i][(length-1)-j],end="")
        print(end=" ")
        for j in range(length):
            print(rectangle[j][(length-1)-i],end="")
    
        print()



