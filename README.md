# Anaton - A very fast anagram solver!

## Installation
Pre-requisites: Python 3.7
```shell script
pip install anaton
```

## Example usage
Below example will print all anagrams of the letters in 'anagram'
```python
from anaton import Dictionary, solve

# Parse a word list
dictionary = Dictionary('wordlist.txt')

# Solve anagrams!
for chunk in solve('anagram', dictionary):
    # The anagram solver will return several anagrams at a time, thus we have to iterate over the chunk returned
    for anagram in chunk:
        print(anagram)
```
