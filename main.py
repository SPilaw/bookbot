from stats import count_words,count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    wordcount = count_words(text)
    print(f"Found {wordcount} total words")
    charcount = count_chars(text)
    print(charcount)

main()


