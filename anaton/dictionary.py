from typing import Optional
from .utils import word_to_number


class Dictionary:
    """
    Reads a word list, finds the numerical representation of all words and groups them in a few different ways.
    """

    def __init__(self, file_name: str, filter_sentence: Optional[str] = None):
        self.words_by_group = {}
        max_length = len(filter_sentence) if filter_sentence else 25
        self.words_by_length = [[] for _ in range(max_length + 1)]
        self.file_name = file_name
        self.parse(filter_sentence)

    def parse(self, filter_sentence: str):
        """
        Parse all words in a word list and populate the instance attributes.

        :param filter_sentence:
        :return:
        """
        if filter_sentence:
            filter_sentence = word_to_number(filter_sentence.lower())
        previous_line = ""
        with open(self.file_name) as f:
            lines = f.read().splitlines()
            lines = zip(lines, map(word_to_number, lines))
            for line, word in lines:
                if len(line) < 2 or line == previous_line:
                    continue
                if not filter_sentence or not(filter_sentence % word):
                    for char in line:
                        if not (97 <= ord(char) <= 122):
                            break
                    else:
                        if not str(word) in self.words_by_group:
                            self.words_by_group[str(word)] = []
                            self.words_by_length[len(line)].append(word)
                        self.words_by_group[str(word)].append(line)
                        previous_line = line

        for i in range(len(self.words_by_length)):
            self.words_by_length[i].sort()
