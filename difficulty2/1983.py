# -*- coding: utf-8 -*-

import sys
sys.stdin = open("1983input.txt", "r")

# 조교의 성적 매기기

# 학점은 상대평가로 총 10개(A+ ~ D0)
# [A+, A0, A-, B+, B0, B-, C+, C0, C-, D0]
# 총점 = 중간고사(35%) + 기말고사(45%) + 과제(20%)
# 10개의 평점을 총점이 높은순서대로 부여하며 각 평점은 같은 비율로 부여할 수 있다
# ex) N명의 학생이 있으면 N/10명의 학생들에게 동일한 평점 부여 가능
# 입력으로 각 학생들의 중간, 기말, 과제점수가 주어짐
# 학점을 알고싶은 K번째학생의번호가 주어지면 학점을 출력하는 프로그램 작성

# [제약사항]
# N은 항상 10의 배수이며, 10이상 100이하의 정수
# K는 1이상 N 이하의 정수 (1 <= K <= N)
# K번째 학생의 총점과 다른학생의 총점이 동이란 경우는 입력으로 주어지지 않는다.

count = int(input())

for test_count in range(1, count+1):
    N_, K_ = tuple(map(int, input().split(' ')))
    
    scores = [] # students' scores
    results = [] # final scores of students
    sorted_lists = []
    
    ranking = [] #rank the students
   
    for _ in range(N_):
        scores.append( list(map(int, input().split())))
    # print('#{} {} {} {}'.format(test_count, N_, K_, scores))
    # #1 10 2 [[87, 59, 88], [99, 94, 78], [94, 86, 86], [99, 100, 99], [69, 76, 70], 
    # [76, 89, 96], [98, 95, 96], [74, 69, 60], [98, 84, 67], [85, 84, 91]]
    
    for idx, score in enumerate(scores):
        results.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2)
    
    sorted_lists.copy(results)
    
    for sorted_result in sorted_lists:
        ranking.append(results.index(sorted_result))

    print(ranking)

    # for _ in range(N_):
    #     ranking.append(results.index(max(results)))
    #     results.remove(max(results))
    
    # print(ranking)