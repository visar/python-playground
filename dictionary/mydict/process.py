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
        try:
            return cls.dictionary[word]
        except KeyError:
            matches = get_close_matches(word, cls.dictionary.keys())
            try:
                candidate = matches[0]
                anwser = input(
                    "Did you mean {} instead? Enter Y if yes, or N if no: ".
                    format(candidate)).lower()

                while anwser not in ['y', 'n']:
                    print("Please anwser Y or N: ")
                    anwser = input().lower()

                if anwser == 'y':
                    return cls.dictionary[candidate]
                elif anwser == 'n':
                    raise MatchNotFoundError

            except (IndexError, MatchNotFoundError) as e:
                return "The word doesn't exist"


class MatchNotFoundError(Exception):
    pass


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
