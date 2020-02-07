PRIME_LIST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131]


def word_to_number(word: str) -> int:
    """
    Converts a word into a numerical representation

    :param word:
    :return:
    """
    value = 1
    for char in word:
        idx = ord(char) - 97
        if idx < 0 or idx > 25:
            continue
        value *= PRIME_LIST[idx]
    return value


def contains(letter_set1: int, letter_set2: int) -> bool:
    """
    Check if a set of letters contains another set of letters.

    :param letter_set1:
    :param letter_set2:
    :return:
    """
    return not(letter_set1 % letter_set2)
