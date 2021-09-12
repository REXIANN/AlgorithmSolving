def solution(s):
    answer = []
    num_dict = { 
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    index = 0
    while index < len(s):
        if s[index].isdigit():
            answer.append(s[index])
            index += 1
        else:
            for inner_index in range(index + 1, index + 6):
                number = s[index:inner_index]
                if num_dict.get(number):
                    answer.append(num_dict[number])
                    index = inner_index
                    break

    return ''.join(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))