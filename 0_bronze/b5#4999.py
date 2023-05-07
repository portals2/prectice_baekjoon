# from collections import deque
# import sys
# input=sys.stdin.readline

a = input()
b = input()

if (b[-1] == 'h') and (a[-1] == 'h'):
    if len(a) >= len(b):
        print('go')
    else:
        print('no')
else:
    print('no')
