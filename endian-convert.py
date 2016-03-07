#!/usr/bin/env python2
import sys


def main():
    opts = filter(lambda x: '-' in x[0], sys.argv)
    args = sys.argv[2:]

    if '-b' in opts:
        convert_big(args)
    if '-s' in opts:
        convert_small(args)


def convert_big(string):
    try:
        output = int(string[0])
        print '0|0|0|' + str(output)
    except ValueError:
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
    try:
        output = int(string[0])
        print '0|0|0|' + str(output)
    except ValueError:
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
