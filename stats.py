"""Stats for messing with text."""

def number_of_words(file_contents:str) -> int:
    """Get total number of words in the text file."""
    word_list = file_contents.split()
    num_words = len(word_list)
    return num_words

def number_of_characters(file_contents: str) -> dict:
    text = file_contents.lower()
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    counts = {}
    for ch in text:
        if ch in alpha:
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def sortkey(items):
    """sortkey for num of chardict"""
    return items["num"]

def num_of_chardict(file_contents: str) -> list:
    charnum = number_of_characters(file_contents)
    diction = [{"char": k, "num": v} for k, v in charnum.items()]
    diction.sort(reverse=True, key=sortkey)
    return diction

def num_chars(file_contents:str):
    r"""Uses num_of_dict to get list of dicts arranged serially then make a list to
     append each dict's 'char' and 'num' as str. Then joins them into one singular
     string with \n"""
    num_dicts = num_of_chardict(file_contents)
    lines = []
    for i in num_dicts:
        lines.append(f"{i['char']}: {i['num']}")
    return "\n".join(lines)
