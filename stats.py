"""Stats for messing with text."""

def get_book_text() -> str:
    """Gets the text from the book as file_contents."""
    path = "/mnt/c/Users/user1/Desktop/bootdotdev/bookbot/books/frankenstein.txt"
    with open(file=path ,encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def number_of_words() -> int:
    """Get total number of words in the text file."""
    file = get_book_text()
    word_list = file.split()
    num_words = len(word_list)
    return num_words

def number_of_characters() -> dict:
    """Count character numbers dictionary."""
    file: str= get_book_text()
    character_file = file.lower()
    character_dict = {}
    for char in character_file:
        if char not in character_dict:
            character_dict[char] = 1
        else :
            character_dict[char] = character_dict[char] + 1
    return character_dict

def sortkey(items):
    """sortkey for num of chardict"""
    return items["num"]

def num_of_chardict() -> list:
    """Seperate the dict to list of dicst with .items and then sort with .sort"""
    charnum = number_of_characters()
    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    diction = []
    for k,v in charnum.items():
        if k in alpha:
            diction = diction + [{"char":k,"num":v}]
    diction.sort(reverse=True,key=sortkey)
    return diction

def num_chars():
    r"""Uses num_of_dict to get list of dicts arranged serially then make a list to
     append each dict's 'char' and 'num' as str. Then joins them into one singular
     string with \n"""
    num_dicts = num_of_chardict()
    lines = []
    for i in num_dicts:
        lines.append(f"{i['char']}: {i['num']}")
    return "\n".join(lines)
