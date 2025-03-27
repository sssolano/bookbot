import sys
import os

from stats import count_words
from stats import number_char
from stats import sorted_dictionarie

def get_book_text():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("The file does not exist. Please provide a valid path.")
        sys.exit(1)
    
    with open(file_path) as f:
        file_read = f.read()
    
    return file_read


def main():
    book_text = get_book_text()
    word_count = count_words(book_text)
    char_counted = number_char(book_text)
    counted_char = sorted_dictionarie(char_counted)
    print("Usage: python3 main.py <path_to_book>")
    print("============ BOOKBOT =========== ")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")   
    print("--------- Character Count -------")   
    for char_dict in counted_char:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")
    print("============= END ===============")

    
main()