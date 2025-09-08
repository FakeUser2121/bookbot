"""This is the main file."""
from stats import number_of_words ,num_chars

def main():
    """Main Function"""
    num_words = number_of_words()
    num_char = num_chars()

    print(
        f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------"""
        )
    print(num_char)

main()
