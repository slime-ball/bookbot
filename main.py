import sys

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
    contents = get_book_text(book)
    num_words = get_num_words(contents)
    count_char = get_num_char(contents)
    sorted = sorted_list(count_char)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for item in sorted:
        current_char = item["char"]
        current_count = item["num"]
        print (f"{current_char}: {current_count}")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words
from stats import get_num_char
from stats import sorted_list

main()