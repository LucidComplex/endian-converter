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
        output = pad_output(string[0])
        print_output(output)


def convert_small(string):
    if is_integer(string):
        handle_integer(string)
    else:
        output = pad_output(string[0])
        print_output(output, big=False)


def print_output(input, big=True):
    length = len(input)
    x = 0
    while x < length:
        if big:
            print_big_output(input, x)
        else:
            print_small_output(input, x)
        x = x + 4


def print_big_output(input, x):
    print '|'.join(input[x:x+4])


def print_small_output(input, x):
    print '|'.join(reversed(input[x:x+4]))


def pad_output(input):
    length = len(input)
    # closest multiple of 4
    x = 0
    while x < length:
        x = x + 4
    return input.ljust(x, '0')



if __name__ == '__main__':
    main()
