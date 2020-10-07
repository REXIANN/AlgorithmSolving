#1288. 새로운 불면증 치료법

import sys
sys.stdin = open("1288input.txt", "r")

# 민석이는 불면증에 걸려서 누워서 양을 센다
# 1번부터 세는것이 아니라 N의 배수번호인 향을 세기로 했다.
# 첫번쨰에는 N번향, 두번째는 2N번 양.. k번쨰에는 kN번쨰양을 센다.
# 이전에 셌던 번호들의 각자리수에서 0부터9까지의 모든 숫자를 보는 것은
# 최쇠 몇번의 양을 센 시점일까?

# N=1259인경우 다섯번째에서 0부터9까지의 모든 숫자를 보게되므로 멈춘다.
# N은 1보다 크고 1,000,000 보다 작다.

tc = int(input())

for test_count in range(1, tc + 1):
    number = int(input())
    index = 1
    number_set = set()

    while True:
        number_string = str(index * number)
        for string in number_string:
            number_set.add(string)
        
        if len(number_set) >= 10:
            break
        index += 1
    
    print('#{} {}'.format(test_count, index * number))    