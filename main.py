"""This is the main file."""
from stats import number_of_words , number_of_characters
num_chars = number_of_characters()
num_words = number_of_words()

def main():
    """Main Function"""
    print(f"{num_words} words found in the document")
    print(num_chars)

main()
