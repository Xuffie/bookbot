import sys
from stats import word_counter
from stats import letter_counter
from stats import sort_letters

# main function that gathers data
def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = word_counter(text)
    char_dict = letter_counter(text)
    sorted_char_list = sort_letters(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for listed_dict in sorted_char_list:
        char = listed_dict["char"]
        num = listed_dict["num"]
        if char.isalpha() == True:
            print(f"{char}: {num}")
    print("============= END ===============")

    

    # print(f"{num_words} words found in the document.")
    # print(f"{char_dict}")


# obtains the text for the book
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
        

main()
