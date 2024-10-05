def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    words = get_text_length(text)
    char_count = get_character_count(text)
    generate_report(words, char_count)

def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def get_text_length(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
        
    return characters

def sort_dict(dictionary):
    # reorder dictionary
    # returns a list of tuples for each key value pair sorted in descending order
    sorted_list = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    
    # convert list back to dictionary
    return dict(sorted_list)

def generate_report(words, char_count):
    sorted_char_count = sort_dict(char_count)

    print("------ Start of Report for Frakenstein.txt ------")
    print(f"Total of {words} found in the document \n")

    for char in sorted_char_count:
        if char.isalpha():
            print(f"The {char} character is found {sorted_char_count[char]} times!")

    print("------ End of Report ------")



main()