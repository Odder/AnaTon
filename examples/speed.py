from anaton import solve
import time


if __name__ == '__main__':
    anagram = 'Anaton analyses speedy'
    print(f'original sentence: "{anagram}"')
    k = 0
    target = 4000000

    solve_generator = solve(anagram, min_word_length=2)
    start = time.time()
    for anagrams in solve_generator:
        k += len(anagrams)
        if k >= target:
            break

    timing = time.time() - start
    print(f'{k} anagrams found in {timing:.3f}s @ {k / timing / 1000:.0f} anagrams/ms.')
    print(f'last anagram was: {anagrams[0]}')
