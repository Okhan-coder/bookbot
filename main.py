import statistic

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
        return file_content

def main():
    book=get_book_text("bookbot/books/frankenstein.txt")
    word_count = statistic.get_word(book)
    print(f"{word_count} words found in the document")

main()

