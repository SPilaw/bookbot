from collections import defaultdict

def count_words(text):
    words = text.split()
    wordcount = len(words)
    return wordcount

def count_chars(text):
    lower_text = text.lower()
    chars = defaultdict(int)
    for char in lower_text:
        count = chars.setdefault(char, 0)
        chars[char] += 1
    return chars 