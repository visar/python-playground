import json
import os


class MyDict(object):
    dictionary = dict()

    @classmethod
    def read_file(cls, filename="data.json"):
        data = os.path.dirname(os.path.realpath(__file__))
        data = os.path.abspath(os.path.join(data, os.pardir, filename))

        with open(data) as f:
            cls.dictionary = json.load(f)
            return cls.dictionary

    @classmethod
    def find_word(cls, word, filename="data.json"):
        if not cls.dictionary:
            cls.read_file()
        return cls.dictionary[word]


def main():
    word = input("Enter word: ")
    for item in MyDict.find_word(word):
        print(item)


if __name__ == '__main__':
    main()
