from stats import number_of_words, number_of_characters

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    book = get_book_text("books/frankenstein.txt")

    print(f"Found {number_of_words(book)} total words")

    bookChars = number_of_characters(book)
    print(bookChars)

if __name__ == "__main__":
    main()