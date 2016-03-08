#!/usr/bin/env python2
import sys


def main():
    opts = filter(lambda x: '-' in x[0], sys.argv)
    args = sys.argv[2:]

    if '-b' in opts:
        convert_big(args)
    if '-s' in opts:
        convert_small(args)


def is_integer(string):
    integer = True
    for x in string:
        try:
            _ = int(x)
        except ValueError:
            integer = False
            break
    return integer

def handle_integer(string):
    for num in string:
        x = 0
        binary_string = str(bin(int(num)))[2:].rjust(32, '0')
        out = []
        for x in range(0, 32, 8):
            out.append(str(int(binary_string[x:x+8], 2)))
        print '|'.join(out)

def convert_big(string):
    if is_integer(string):
        handle_integer(string)
    else:
        length = len(string[0])
        # closest multiple of 4
        x = 0
        while x < length:
            x = x + 4
        output = string[0].ljust(x, '0')
        x = 0
        while x < length:
            print '|'.join(output[x:x+4])
            x = x + 4


def convert_small(string):
    if is_integer(string):
        handle_integer(string)
    else:
        length = len(string[0])
        # closest multiple of 4
        x = 0
        while x < length:
            x = x + 4
        output = string[0].ljust(x, '0')
        x = 0
        while x < length:
            print '|'.join(reversed(output[x:x+4]))
            x = x + 4



if __name__ == '__main__':
    main()
