# 다트게임.py
def solution(dartResult):
    scores = []
    bonuses = []
    number = []
    for char in dartResult:
        if char.isdigit():
            number.append(char)
        else:
            bonuses.append(char)
            if number:
                scores.append(int(''.join(number)))
                number = []

    print(scores, bonuses)
    idx1 = 0
    idx2 = 0
    while idx2 < len(bonuses):
        target = bonuses[idx2]
        if target == 'S':
            scores[idx1] = scores[idx1] ** 1
        elif target == 'D':
            scores[idx1] = scores[idx1] ** 2
        elif target == 'T':
            scores[idx1] = scores[idx1] ** 3
        else:
            raise Exception('Not a valid score.')
        
        if idx2 + 1 < len(bonuses) and not bonuses[idx2 + 1].isalpha():
            idx2 += 1
            target = bonuses[idx2]
            if target == '#':
                scores[idx1] = -scores[idx1]
            elif target == '*':
                scores[idx1] *= 2
                if idx1 - 1 >= 0:
                    scores[idx1 - 1] *= 2
            else:
                raise Exception('Not a valid bonus mark.')
        idx2 += 1
        idx1 += 1

    return sum(scores)


dartResult = '1D2S#10S'
print(solution(dartResult))