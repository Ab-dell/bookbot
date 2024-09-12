path_to_file = "books/frankenstein.txt"

def get_number_of_word(string):
    words = string.split()
    i = 0
    for word in words:
            i += 1
    print(f"there is {i} words in the document")
    return i

def get_occurences_of_character(string):
    chars = {}
    for word in string:
        lowered_word = word.lower()
        if lowered_word in chars:
             chars[lowered_word] += 1
        else:
             chars[lowered_word] = 1
        
    keys_from_dict = chars.keys()
    values_from_dict = chars.values()
    # keys_from_dict.sort()
    print(f"list_from_dict: {keys_from_dict}")
    # for item in list_from_dict:
    #     if item[0].isalpha():
    #         print(f"The {item[0]} character was found {item[1]} times")


    # print(f"chars: {chars}")
    return chars     

      

def main():
    print(f"--- Begin report of {path_to_file} ---")
    with open(path_to_file) as f:
            file_content = f.read()
            get_number_of_word(file_content)
            get_occurences_of_character(file_content)

main()