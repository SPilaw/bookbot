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

def sort_on(items):
    return items["num"]

def sort_charcount(dict):
    list_of_dicts = []
    for key in dict:
        list_of_dicts.append({"char": key, "num": dict[key]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
    
