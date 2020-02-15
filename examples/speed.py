from anaton import Dictionary, solve
import time


if __name__ == '__main__':
    anagram = 'This is a long string'
    print(f'original sentence: "{anagram}"')
    k = 0
    target = 100000

    solve_generator = solve(anagram, min_word_length=3)
    start = time.time()
    for anagrams in solve_generator:
        k += len(anagrams)
        if k >= target:
            timing = time.time() - start
            print(f'{target} anagrams found in {timing:.3f}s @ {target / timing / 1000:.0f} anagrams/ms.')
            targets = []
            break

    print(f'last anagram was: {anagrams[0]}')
