def solution(s):
    answer = list(map(int, s.split(' ')))
    return " ".join([str(min(answer)), str(max(answer))])