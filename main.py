def main():
    #Opens files and reads contents of book
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()

    #Displays contents to the console
    print(book_contents)

    
main()