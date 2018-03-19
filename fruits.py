#!/usr/bin/env python


def process_fruits(filename="fruits.txt"):
    with open(filename) as f:
        text = f.read()
        return text.splitlines()


def fruit_lengths(filename="fruits.txt"):
    fruits = process_fruits()
    return {fruit: len(fruit) for fruit in fruits}


if __name__ == '__main__':
    for fruit, fruit_length in fruit_lengths().items():
        print("{fruit} {fruit_length}".format(
            fruit=fruit, fruit_length=fruit_length))
