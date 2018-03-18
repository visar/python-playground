#!/usr/bin/env python


def process_fruits(filename="fruits.txt"):
    with open(filename) as f:
        text = f.read()
        return text.splitlines()


if __name__ == '__main__':
    for line in process_fruits():
        print(line)
