# 오픈채팅방
def solution(record):
    actions = []
    user = {}
    for rec in record:
        rec = tuple(rec.split())
        if len(rec) == 3:
            action, uid, name = rec
            if action[0] == 'E':
                actions.append(('E', uid))
            user[uid] = name
        else:
            action, uid = rec
            actions.append(('L', uid))
    
    return [user.get(act[1]) + '님이 들어왔습니다.' if act[0] == 'E' else user.get(act[1]) + '님이 나갔습니다.' for act in actions]


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]

print(solution(record))
