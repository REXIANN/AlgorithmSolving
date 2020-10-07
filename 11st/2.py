# -*- encoding: utf-8 -*-

def solution(S):
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            for k in range(len(S[i])):
                if S[i][k] == S[j][k]:
                    return [i, j, k]
    return []
