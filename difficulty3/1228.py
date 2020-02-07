# 1228.py 암호문1
import pprint
import sys
sys.stdin = open("1228input.txt", "r")

# I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다.
#  s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
# 위의 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때, 
# 암호문을 수정하고, 수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라.

# 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)
# 두 번째 줄 : 원본 암호문
# 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)
# 네 번째 줄 : 명령어

tc = 10
for test_count in range(1, tc + 1):
    len_original_code = int(input())
    original_code = list(map(int, input().split()))
    num_commands = int(input())
    commands = list(input().split('I'))
    original_code = original_code[0:10]

    # commands 리스트를 깔끔하게 정리
    commands.pop(0)
    for i in range(len(commands)):
        commands[i] = commands[i].strip()
    
    #pprint.pprint(commands)
    # ['1 5 400905 139831 966064 336948 119288',
    # '8 6 436704 702451 762737 557561 810021 771706']

    for i in range(num_commands):
        command_list = list(map(int, commands[i].split()))
        #print('command list:', command_list)
        # [1, 5, 400905, 139831, 966064, 336948, 119288]

        if command_list[0] >= 10: # 이게 맞음
            continue
        
        idx = 2
        if command_list[0] + command_list[1] > 10: # 이게 맞음. [8,3]은 8, 9 만 들어간다
            for j in range(command_list[0], 10): 
                original_code[j] = command_list[idx]
                idx += 1
        else:
            for j in range(command_list[0], command_list[0] + command_list[1]):
                original_code[j] = command_list[idx]
                idx += 1
    
    print('#{}'.format(test_count), end=" ")
    for val in original_code:
        print(val, end=" ")
    print()