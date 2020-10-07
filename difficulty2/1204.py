# 1204.py 최빈수 구하기

import sys
sys.stdin = open("1204input.txt", "r")

# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 
# 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
# 다음과 같은 수 분포가 있으면,
# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
# 최빈수는 8이 된다.
# 최빈수를 출력하는 프로그램을 작성하여라
# 학생수는 1000명이며 각 학생의 점수는 0 ~ 100점 사이이다.

tc = int(input())

for test_count in range(1, tc + 1):
    count = int(input())
    scores = list(map(int, input().split()))
    notes = [0] * 101 # 점수는 0 ~ 100점 사이
    # print(scores[:10])

    for score in scores:
        notes[score] += 1
    #print(notes)

    frequent_value = 0
    frequent_idx = 0
    
    for idx, note in enumerate(notes):
        if note >= frequent_value:
            frequent_value = note
            frequent_idx = idx

    print('#{} {}'.format(count, frequent_idx))
