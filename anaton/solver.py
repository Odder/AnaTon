from collections import deque
from itertools import permutations, product
from typing import List
from .utils import word_to_number, contains
from .dictionary import Dictionary


def solve(letters: str, dictionary: Dictionary) -> List[str]:
    """
    A BFS anagram solver that checks every candidate up against a lookup table of depth 1.

    The anagram solver represents all letter sets as a number. Every character in a word is represented by a prime
    number, then a set of letters is represented by the product of all the character-primes.
    The algorithm then searches for different factorisations of the input letter set based on the factor set from the
    dictionary.

    When a match has been found it then converts the factors back into all the words represented by that factor and
    yields all possible permutations of those words separated by spaces.

    :param letters:
    :param dictionary:
    :return:
    """
    letters_numerical = word_to_number(letters)
    queue = deque()
    queue.append((word_to_number(letters), len(letters), []))

    if str(letters_numerical) in dictionary.words_by_group:
        candidates = cartesian_solutions([letters_numerical], dictionary)
        yield candidates

    while queue:
        letters, length, path = queue.popleft()

        for i in range(length):
            for word_letters in dictionary.words_by_length[length - i]:
                if path and word_letters > path[-1]:
                    continue
                if contains(letters, word_letters):
                    remaining_letters = letters // word_letters
                    if str(remaining_letters) in dictionary.words_by_group:
                        candidates = cartesian_solutions(path + [word_letters] + [remaining_letters], dictionary)
                        yield candidates
                    queue.append((letters // word_letters, i, path + [word_letters]))


def cartesian_solutions(path: List[int], dictionary: Dictionary) -> List[str]:
    """
    Finds all words in the dictionary matching the factor and returns all permutations of the cartesian product of
    said words.

    :param path:
    :param dictionary:
    :return:
    """
    words = [dictionary.words_by_group[str(idx)] for idx in path]
    solutions = []
    for permutation in permutations(words):
        solutions.extend([' '.join(c) for c in product(*permutation)])
    return solutions
