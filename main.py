def main():
    #Opens files and reads contents of book
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()

    total_word_count = word_count(book_contents)
    print(total_word_count)
    #Displays contents to the console
    

def word_count(full_text):
    amount_of_words = 0
    words = full_text.split()
    for x in range(0, len(words)):
        amount_of_words += 1

    return amount_of_words
    
main()