from operator import mul
from functools import reduce

PRIME_MAP = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37,
              'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83,
              'x': 89, 'y': 97, 'z': 101}


def word_to_number(word: str) -> int:
    """
    Converts a word into a numerical representation

    :param word:
    :return:
    """
    value = 1
    for char in word:
        value *= PRIME_MAP[char] if char in PRIME_MAP else 1
    return value


def strip(word: str) -> str:
    """
    Converts a word into a numerical representation

    :param word:
    :return:
    """
    stripped_word = ""
    for char in word:
        if 97 <= ord(char) <= 122:
            stripped_word += char
    return stripped_word
