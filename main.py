def get_book_text(file_path):
    with open(file_path) as f:
        print (f.read())
    return 0

get_book_text("books/frankenstein.txt")
