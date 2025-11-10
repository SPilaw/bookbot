def count_words(text):
    words = text.split()
    wordcount = len(words)
    return wordcount

def count_chars(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars 
