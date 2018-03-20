import json
import os

from difflib import get_close_matches


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
        word = word.lower()
        if word in cls.dictionary:
            return cls.dictionary[word]
        elif len(get_close_matches(word, cls.dictionary.keys())) > 0:
            anwser = input(
                "Did you mean {} instead? Enter Y if yes, or N if no: ".format(
                    get_close_matches(word, cls.dictionary.keys())[0]))
            if anwser in ['Y', 'y']:
                return cls.dictionary[
                    get_close_matches(word, cls.dictionary.keys())[0]]
            elif anwser in ['N', 'n']:
                return "The word doesn't exist"
            else:
                return "Please anwser Y or N"
        else:
            return "The word doesn't exist"


def main():
    word = input("Enter word: ")
    output = MyDict.find_word(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)


if __name__ == '__main__':
    main()
