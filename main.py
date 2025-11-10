from stats import count_words,count_chars,sort_charcount

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
    sorted_list = sort_charcount(charcount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
main()


