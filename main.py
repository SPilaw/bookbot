from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book = "books/frankenstein.txt"
    text = get_book_text("books/frankenstein.txt")
    wordcount = count_words(text)
    print(f"Found {wordcount} total words")
main()


