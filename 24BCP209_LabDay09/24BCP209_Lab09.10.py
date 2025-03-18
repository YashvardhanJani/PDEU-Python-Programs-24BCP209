# 10. Write a program that defines a function called frequency() which computes the frequency of words present in a string passed to it. The frequencies should be returned in sorted order of words in the string.

from collections import Counter

def frequency(s):
    words = s.lower().split()
    word_counts = Counter(words)
    sorted_word_counts = dict(sorted(word_counts.items()))
    return sorted_word_counts

text = "This is a test. This test is simple."
print(frequency(text))
