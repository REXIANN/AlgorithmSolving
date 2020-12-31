# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요

# [Notice for Python3]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요 
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
# - 입력과 출력은 input()과 print()를 사용하세요

from collections import deque
	
#가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
	# <---메인 코드의 시작---> 
	dq = deque()
	N = 0
	
	for _ in range(int(input())):
		user_input = list(input().split())

		if user_input[0] == 'PUSH':
			dq.append(user_input[1])
			dq = deque(sorted(list(dq)))
			N = dq[len(dq) // 2] if len(dq) % 2 else dq[(len(dq) - 1) // 2]
			print(N)
		
		elif user_input[0] == 'POP':
			if dq:
				dq.remove(N)				
			if not dq: 
				print('NO ITEM')
			else:
				dq = deque(sorted(list(dq)))
				N = dq[len(dq) // 2] if len(dq) % 2 else dq[(len(dq) - 1) // 2]
				print(N)
		else:
			print(len(dq))
		
		
	# <---메인 코드의 끝---> # for a new test
