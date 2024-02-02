#!/usr/bin/env python3

def print_fibonacci(length):
    printer = [0, 1]
    for i in range(1, length - 1):
        printer.append(printer[i - 1] + printer[i])
    print(printer[0 : length])

print_fibonacci(4)