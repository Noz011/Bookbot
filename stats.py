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

def sorted_char_dic(dic):
    sorted_dic = []
    count = 0
    for key in dic:
        sorted_dic.append({})
        sorted_dic[count]["char"] = key
        sorted_dic[count]["num"] = dic[key]
        count+= 1
    return sorted_dic
        
def sort_on(e):
    return e["num"]

def toString(dicList, filepath, book):
    print("============ BOOKBOT ============\n"
        f"Analizing book found at {filepath}...\n"
        "----------- Word Count ----------\n"
        f"Found {number_of_words(book)} total words\n"
        "--------- Character Count -------")
    for dic in dicList:
            print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")
