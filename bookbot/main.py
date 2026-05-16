import sys
from stats import count_words, count_characters, sort_dictionary, print_report, sort_on, print_dictionary


def get_book_text(filepath):
    # Take filepath as input and returns contents of file as a string.

    # print(f"Now getting file path for file at: {filepath} ")

    # print("Opening File...")

    with open(file=filepath) as f:

        file_content: str = f.read()

        # print("Now printing file content...")

        return file_content
    

def main():
    
    ## Check if have req'd cli args

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    ## Get filepath from sys

    filepath: str = sys.argv[1]

    ## Get book text

    book_text: str = get_book_text(filepath)
    word_count = count_words(book_text)
    list_of_dictionaries = count_characters(book_text)

    sorted_dictionary = sort_dictionary(list_of_dictionaries)

    # print("---DEBUG---")
    # print(sorted_dictionary)
    # print("---DEBUG---")

    report_string = print_dictionary(sorted_dictionary)

    print_report(filepath, word_count, report_string)
    
main()