from stats import get_words, get_letters,sort_print
import sys
def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book=get_book_text(sys.argv[1])
    print(f"Analyzing book found at: {sys.argv[1]}")
    word_count = get_words(book)
    print("----------- Word Count ----------")
    print(f" Found {word_count} total words ")
    char_dict = get_letters(book)
    sort_print(char_dict)
    return
main()
