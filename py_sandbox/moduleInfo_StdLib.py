'''
objective: explain esoteric parts of the builtin modules of python
'''

# 01 Strings =======================================================================================

# 1.01 Formatting Strings ==================================
# source: https://docs.python.org/3.4/library/string.html#format-string-syntax
a = 10.124835429
b = 'test'
print('basic   : {}'.format(a))
print('round   : {:.2f}'.format(a))
print('scienti : {:e}'.format(a))
print('sci+rnd : {:.2e}'.format(a))
print('integer : {:d}'.format(int(a))) # if don't convert, get an error
print('percent : {:.2%}'.format(a))
print('readable: {:,}'.format(round(a*1e6)))
print('Lpad    : |{:>8}|'.format(b))
print('Rpad    : |{:<8}|'.format(b))
print('Cpad    : |{:^8}|'.format(b))
print('pad spec: |{:+^8}|'.format(b)) # charcter before '^' will be repeated everywhere

# classic example: lpad with zeros:
print('typical : {:0>3}'.format(3))
# another way to pad strings

print('text with rpad '.ljust(30,'-'))


# 02 Windows Command Line  =========================================================================

import os

# 2.01 Get Command Line output as string ===============================
x = os.popen('echo hello').read()
print(x)

# 03 Bytes<>Ints<>Hex =============================================================
'''
want to understand how bytes are manipulated & converted in python
DO NOT USE "hex()"! THIS ONLY RETURNS A NORMAL STRING OF WHAT A DECIMAL VALUE LOOKS LIKE AS A HEX
'''

# alphanumeric data
bytestr = b'this' # print() => b'this' # note: string of bytes
normstr = bytestr.decode() # print() => 'this' # normal string
bytestr2 = normstr.encode() # back to a bytestr
print(bytestr)

# note that mixing encodings can lead to incorrect-looking data
print(
    (chr(0).encode('utf-16')+'this'.encode()).decode('utf-16')
)

# numeric data: switch from between: decimal <=> hex <=> binary <=> decimal
# ex: 165 = 1010 0101 = 0xA5. want to pull out exact values from each place
valint=165
valhex=b'\xa5' # 165
valbin='0b10100101'

# how to swap between each:
print('as int :',valint)
print('int2hex:',valint.to_bytes(1,'little'))
print('int2bin:',bin(valint))
print('---')
print('as hex :',valhex)
print('hex2int:',int.from_bytes(valhex,'little'))
print('hex2bin:',bin(int.from_bytes(valhex,'little')))
print('---')
print('as bin :',valbin)
print('bin2int:',int(valbin,2))
print('bin2hex:',int(valbin,2).to_bytes(1,'little'))

# eof





