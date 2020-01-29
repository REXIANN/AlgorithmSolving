# -*- coding: utf-8 -*-

# 파리퇴치

# N*N 의 배열안에 숫자가 존재하며 그 숫자는 해당영역의 파리의 숫자
# M*M 크기의 파리채를 내리쳐 파리를 죽인다.

#총 횟수 입력 받음
count = int(input())

for nm in range(count):
    #맵의 크기와 파리채의 크기 입력받음. 튜플로 저장 후 변수에 분배
    tuple_ = ()
    tuple_ += tuple(input().split(' '))

    N_ = int(tuple_[0]) # 맵의 크기 N*N
    M_ = int(tuple_[1]) # 파리채의 크기 M*M
    map_ = []
    result = []
    sum = 0

    for _ in range(N_):
        map_.append(list(input().split(' ')))
    # # N*N크기의 맵에 변수들넣음. 리스트 안의 스트링 리스트 형태
    # [['1', '3', '3', '6', '7'], ['8', '13', '9', '12', '8'], 
    # ['4', '16', '11', '12', '6'], ['2', '4', '1', '23', '2'],
    #  ['9', '13', '4', '7', '3']]

    margin = N_ - M_

    for i in range(margin + 1):
        for j in range(margin + 1):
            for k in range(M_):
                for m in range(M_):        
                    sum += int(map_[i+k][j+m])
            result.append(sum)
            sum = 0

    print(f'#{nm+1} {max(result)}')