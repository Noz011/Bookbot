def number_of_words(book:str):
    wordList =book.split()
    return len(wordList)

def number_of_characters(book:str):
    book = book.lower()
    charDict = {}
    for char in book:
        if not char in charDict:
            charDict[char] = 1
        else:
            charDict[char] = charDict[char] + 1
    return charDict