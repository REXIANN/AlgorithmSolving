def solution(s):
    slist = []
    flag = False
    for ss in s:
        if flag:
            slist.append(ss.upper())
            flag = False
        else:
            slist.append(ss.lower())
        if ss == ' ':
            flag = True
            
    if slist[0].isalpha():
        slist[0] = slist[0].upper()
    return ''.join(slist)