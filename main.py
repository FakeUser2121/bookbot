"""This is the main file."""
import sys

from stats import number_of_words ,num_chars

def main():
    """Main Function"""
    num_words = number_of_words(file_contents)
    num_char = num_chars(file_contents)

    print(
        f"""
============ BOOKBOT ============
Analyzing book found at {BPATH}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------"""
        )
    print(num_char)


if len(sys.argv) == 2:
    BPATH = str(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


with open(file=BPATH ,encoding="utf-8") as f:
    file_contents = f.read()

main()
