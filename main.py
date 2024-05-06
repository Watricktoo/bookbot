def main():
    book_contents = read_book()
    total_word_count = word_count(book_contents)
    letter_dict = count_letters(book_contents)
    

    letter_list_dict = []
    for char in letter_dict:
        new_dict = {"char": char, "count": letter_dict[char]}
        letter_list_dict.append(new_dict)
    
    letter_list_dict.sort(reverse=True, key=sort_on)
    
    formatted_output(total_word_count,letter_list_dict)
    
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
            if chars.isalpha():
                if chars in letter_count:
                    letter_count[chars] += 1
                else: 
                    letter_count[chars] = 1
    return letter_count

def sort_on(letter_dictionary):
    return letter_dictionary["count"]

def formatted_output(word_count, letter_list_dict):
    print(f"{word_count} words found in the document")
    for dict in letter_list_dict:
        print(f"The {dict['char']} character was found {dict['count']} times ")

main()