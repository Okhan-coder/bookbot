from stats import get_words, get_letters,sort_print

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def main():
    book=get_book_text("./books/frankenstein.txt")
    word_count = get_words(book)
    print(f"{word_count} words found in the document")
    char_dict = get_letters(book)
    sort_print(char_dict)
main()

