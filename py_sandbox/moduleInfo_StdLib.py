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

# another way to pad strings

print('text with rpad '.ljust(30,'-'))


# 02 Windows Command Line  =========================================================================

import os

# 2.01 Get Command Line output as string ===============================
x = os.popen('echo hello').read()
print(x)






