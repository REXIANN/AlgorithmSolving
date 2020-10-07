def solution(new_id):
    others = {'-', '_', '.'}
    length = len(new_id)
    id_alpha = [0] * length
    id_others = [0] * length

    # 1, 2
    for i in range(length):
        if new_id[i].isalpha() or new_id[i].isdigit():
            id_lower = new_id[i].lower()
            id_alpha[i] = id_lower
        else:
            id_others[i] = new_id[i]

    for i in range(length):
        if id_others[i] not in others:
            id_others[i] = 0

    new_new_id = [0] * length
    for i in range(length):
        a, b = id_alpha[i], id_others[i]
        if a == 0 and b == 0:
            pass
        else:
            new_new_id[i] = id_alpha[i] if id_alpha[i] else id_others[i]

    n_id = [i for i in new_new_id if i != 0]
    # print('1', n_id)
    # 3
    head, tail = 0, 0
    while head < len(n_id) and tail < len(n_id):
        if n_id[head] == '.':
            tail = head
            while tail + 1 < len(n_id) and n_id[tail + 1] == '.':
                tail += 1

            if head != tail:
                for i in range(head + 1, tail + 1):
                    n_id[i] = 0
        head += 1

    n_id = [i for i in n_id if i != 0]
    # print('2', n_id)
    # 4
    if n_id[0] == '.':
        n_id = n_id[1:]

    # print('3', n_id)
    if len(n_id) > 0 and n_id[-1] == '.':
        n_id = n_id[:-1]

    # 5
    if len(n_id) == 0:
        n_id = ['a']
    # 6
    if len(n_id) > 15:
        n_id = n_id[:15]
        if n_id[0] == '.':
            n_id = n_id[1:]
        if len(n_id) > 0 and n_id[-1] == '.':
            n_id = n_id[:-1]

    # 7
    if len(n_id) == 1:
        last = n_id[0]
        n_id.append(last)
        n_id.append(last)
    elif len(n_id) == 2:
        last = n_id[1]
        n_id.append(last)
    # print(n_id)
    answer = ''.join(n_id)
    return answer


new_id = "abcdefghijklmn.p"
print(solution(new_id))
