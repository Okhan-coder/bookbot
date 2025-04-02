def get_words(book):
    word_list=book.split()
    return len(word_list)
def get_letters(book):
    lowercase_book = book.lower()
    lowercase_book_split = lowercase_book.split()
    char_count = {}
    for word in lowercase_book_split:
        characters = list(word)
        for character in characters:
            if character in char_count:
                char_count[character] +=1
            else:
                char_count[character] = 1
    return char_count
def sort_print(char_dict):
    print("============ BOOKBOT ============")
    sorted_list = []
    for key,value in char_dict.items():
        if key.isalpha():
            sorted_list.append({"character" : key, "count" : value})
    print(sorted_list)