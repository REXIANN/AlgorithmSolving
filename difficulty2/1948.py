# 1948. 날짜 계산기

import sys
sys.stdin = open("1948input.txt", "r")

# 월,일로 이루어진 날짜를 2개 입력받는다
# 두번째 날짜가 첫번째 날짜로부터 며칠째 되는 날인지 출력하는 프로그램을 작성한다
# 1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31
# 두번째 날짜가 첫번째 날짜보다 항상 크게 주어진다

tc = int(input())
# 첫번째월 / 첫번째일 / 두번째월 / 두번째일
calender = {
    '1':31,'2':28,'3':31,'4':30,'5':31,
    '6':30,'7':31,'8':31,'9':30,'10':31,
    '11':30, '12':31
}

for test_count in range(1, tc+1):
    first_month, first_day, second_month, second_day = tuple(map(int, input().split()))
    # print(first_month, first_day, second_month, second_day)
    date = 0

    # 시작월과 끝월이 같다면 일수만 뺀다. 다르면 다음단계로 진행한다
    if first_month == second_month:
        date = second_day - first_day + 1
    else:
        # 시작월과 끝월 사이에 있는 온전한 개월수 구하기
        for i in range(first_month, second_month):
            date += calender[str(i)]
    
        # 끝월 날짜 더해주고 시작월 날짜 빼주기
        date = date + second_day - first_day + 1

    print(date)