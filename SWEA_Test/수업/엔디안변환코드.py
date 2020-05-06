def ce(n):
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i * 8)) & 0xff)
    return p

def ce1(n):
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)

# python에서의 엔디안 변환
import struct
# c로 작성된 구조체와의 호환을 위한 라이브러리. bit-stream 형태로 데이터를 보낼 수 있다.
num = 27
#빅엔디안
res = struct.pack('>i', num)
print("big endian :", res)

#리틀엔디안
res = struct.pack('<i', num)
print("little endian:", res)
