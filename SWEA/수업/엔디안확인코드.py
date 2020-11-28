n = 0x00111111
if n & 0xFF:
    print('little endian')
else:
    print('big endian')

import sys
if sys.byteorder == 'little':
    print("Little endian platform")
else:
    print("Big endian platform")
