from stats import count_words,count_chars,sort_charcount
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    wordcount = count_words(text)
    charcount = count_chars(text)
    sorted_list = sort_charcount(charcount)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

main()


