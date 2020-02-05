# 1928. Base64 Decoder

import sys
sys.stdin = open("1928input.txt", "r")

# 우선 24비트 버퍼에 위쪽부터 한 byte씩 3byte의 문자를 집어넣는다.
# 버퍼의 위쪽부터 6비트씩 잘라 그값을 읽고, 각각의 값을 아래표의 문자로 Encoding한다

### 제약사항 ###
# 문자열의 길이는 항상 4의 배수로 주어진다.
# 문자열의 길이는 100000을 넘지 않는다.

buffer_24bit = {
    'A':  0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
    'F':  5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
    'K': 10, 'L':11, 'M':12, 'N':13, 'O':14, 
    'P': 15, 'Q':16, 'R':17, 'S':18, 'T':19,
    'U': 20, 'V':21, 'W':22, 'X':23, 'Y':24, 
    'Z': 25, 'a':26, 'b':27, 'c':28, 'd':29,
    'e': 30, 'f':31, 'g':32, 'h':33, 'i':34, 
    'j': 35, 'k':36, 'l':37, 'm':38, 'n':39,
    'o': 40, 'p':41, 'q':42, 'r':43, 's':44, 
    't': 45, 'u':46, 'v':47, 'w':48, 'x':49,
    'y': 50, 'z':51, '0':52, '1':53, '2':54, 
    '3': 55, '4':56, '5':57, '6':58, '7':59,
    '8': 60, '9':61, '+':62, '/':63
}

# 10진수를 2진수로 0b없이 바꾸는 방법
# format(42, 'b') = 101010
# '{:08}'.format(7,'b') = 0000 0007

tc = int(input())

for test_count in range(1, tc + 1):
    print('#{}'.format(test_count),end=" ")
    encoded_string = input()
    binary_string = ''
    decoded_string = 'for test'          

    for encoded_char in encoded_string:
       binary_string += '{:06b}'.format(buffer_24bit[encoded_char])
    #    binary_string_test = '{:06b}'.format(buffer_24bit[encoded_char])
    #    binary_string_int = int(binary_string_test, 2) 
    #    print(binary_string_int)

    for i in range((len(encoded_string) * 3) // 4):
        decimal_string = binary_string[8 * i : 8 * i + 8]
        original_string = int(decimal_string, 2)
        print(chr(original_string), end="")
    print()

    

    #######################################
    # for i in range(1<<len(arr)):
    #         six_bit_sum = ''
    #         for j in range(len(arr)):
    #             if (i & (1 << j)): 
    #                 six_bit_sum += '1'
    #             else:
    #                 six_bit_sum += '0'
    #         #print(six_bit_sum)