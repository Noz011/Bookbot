from stats import *
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("Usage: python3 main.py <path_to_book>")
    filepath = sys.argv[1]
    book = get_book_text(filepath)

    bookChars = number_of_characters(book)


    dic = sorted_char_dic(bookChars)
    dic.sort(reverse=True, key=sort_on)
    toString(dic, filepath, book)

    print(sys.argv)
if __name__ == "__main__":
    main()