from itertools import permutations

def solution(board):
    max_value = 0
    for permutation in permutations([i for i in range(len(board))], len(board)):
        total = sum([board[j][permutation[j]] for j in range(len(permutation))])
        max_value = total if total > max_value else max_value
    
    return max_value