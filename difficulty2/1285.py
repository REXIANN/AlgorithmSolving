# 1285. 아름이의 돌 던지기

import sys
sys.stdin = open("1285input.txt", "r")

# 아름이를 포함한 N명의 사람들이 돌던지기 놀이를 한다
# -100000 ~ 100000 사이의 숫자가 일렬로 써 있다
# 사람들은 100000의 위치에 서서 최대한 0에 가깝게 돌을 던진다
# -100000과 100000에도 돌이 떨어질 수 있다
# 돌이 가장 0에 가깝게 떨어진 곳과 0 사이의 거리 차이와 
# 그렇게 던진 사람이 몇 명인지 나타내는 정수를 공백 하나로 구분하여 출력

tc = int(input())

for test_count in  range(1, tc + 1):
    print('#{}'.format(test_count), end=" ")
    N_ = int(input())
    rock_position = list(map(int, input().split()))
    distance, people = 100000, 0
    
    for rock in rock_position:
        
        if rock < 0:
            rock *= -1
       
        if distance > rock: 
            distance = rock
            people = 0
        
        if rock == distance:
            people += 1

    print(distance, people)

####### NOTICE #######
# 최종적으로 결과값이 output.txt와 일치하나
# 컴파일러가 c++만을 지원하고 java와 python은 지원이 안되는 관계로
# 제출은 하지 못하였음