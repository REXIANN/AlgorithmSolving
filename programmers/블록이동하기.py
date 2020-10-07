# 블록 이동하기
# https://programmers.co.kr/learn/courses/30/lessons/60063

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def solution(board):
    max_move = (len(board[0]) - 1) * 2
    stack = [((0, 0), (0, 1))]

    # 내일 2트.. 가자..



    answer = []
    return answer

print(solution(board))
