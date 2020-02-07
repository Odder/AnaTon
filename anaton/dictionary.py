from .utils import contains, word_to_number
from typing import Optional


class Dictionary:
    """
    Reads a word list, finds the numerical representation of all words and groups them in a few different ways.
    """

    def __init__(self, file_name: str, filter_sentence: Optional[str] = None):
        self.words_by_group = {}
        max_length = len(filter_sentence) if filter_sentence else 25
        self.words_by_length = [[] for _ in range(max_length)]
        self.file_name = file_name
        self.parse(filter_sentence)

    def parse(self, filter_sentence: str):
        """
        Parse all words in a word list and populate the instance attributes.

        :param filter_sentence:
        :return:
        """
        if filter_sentence:
            filter_sentence = word_to_number(filter_sentence)
        previous_line = ""
        with open(self.file_name) as f:
            for line in f:
                line = line[:-1]
                if len(line) < 2 or line == previous_line:
                    continue
                word = word_to_number(line)
                if not filter_sentence or contains(filter_sentence, word):
                    for char in line:
                        if not (97 <= ord(char) <= 122):
                            break
                    else:
                        if not str(word) in self.words_by_group:
                            self.words_by_group[str(word)] = []
                            self.words_by_length[len(line)].append(word)
                        self.words_by_group[str(word)].append(line)
                        previous_line = line
