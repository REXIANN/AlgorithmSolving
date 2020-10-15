def solution(phone_book):
    length = list(set(len(phone) for phone in phone_book))
    phone_dict = {phone: True for phone in phone_book}
    print(phone_dict)
    for phone in phone_book:
        for l in length:
            if len(phone) > l:
                elem = phone[:l]
                if phone_dict.get(elem):
                    print(phone, elem)
                    return False
    return True


phone_book = ['1111113', '1112', '12']
print(solution(phone_book))
