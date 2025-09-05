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
    character_list = file.lower()
    character_dict = {}
    for char in character_list:
        if char not in character_dict:
            character_dict[char] = 1
        else :
            character_dict[char] = character_dict[char] + 1
    return character_dict