def main():
    book_contents = read_book()
    total_word_count = word_count(book_contents)
    letter_dict = count_letters(book_contents)
    formated_output(total_word_count, letter_dict)
    #Displays contents to the console
    

def word_count(full_text):
    amount_of_words = 0
    words = full_text.split()
    for x in range(0, len(words)):
        amount_of_words += 1

    return amount_of_words

def read_book():
    #Opens files and reads contents of book
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    return book_contents

def count_letters(full_text):
    letter_count = {}
    lowercase_text = full_text.lower()
    for words in lowercase_text:
        for chars in words:
            if chars in letter_count:
                letter_count[chars] += 1
            else: 
                letter_count[chars] = 1
    return letter_count
    
def formated_output(word_total, letter_dictionary):
    print(word_total)
    print(letter_dictionary)
main()