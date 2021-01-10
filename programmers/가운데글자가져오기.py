def solution(s):
    moitie = len(s) // 2
    
    if len(s) % 2 != 0:
        answer = str(list(s)[moitie])
    elif len(s) % 2 == 0:
        answer = str(list(s)[moitie -1] + list(s)[moitie])
    return answer