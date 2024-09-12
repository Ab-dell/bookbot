path_to_file = "books/frankenstein.txt"

def get_number_of_word(string):
    words = string.split()
    i = 0
    for word in words:
            i += 1
    print(f"there is {i} words in the document")
    return i    

def sort_on(dict):
    return dict["value"]

def get_sorted_list_from_dict(dict):
    sorted_list = []
    for key in dict:
        if key.isalpha():
            sorted_list.append({"key": key, "value":dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    # print(sorted_list)
    return sorted_list


def get_occurences_of_character(string):
    chars = {}
    for word in string:
        lowered_word = word.lower()
        if lowered_word in chars:
             chars[lowered_word] += 1
        else:
             chars[lowered_word] = 1
    
    sorted_list = get_sorted_list_from_dict(chars)
    for item in sorted_list:
        print(f"The {item['key']} character was found {item['value']} times")
    
    return chars 

      

def main():
    print(f"--- Begin report of {path_to_file} ---")
    with open(path_to_file) as f:
            file_content = f.read()
            get_number_of_word(file_content)
            # get_occurences_of_character(file_content)
            get_sorted_list_from_dict(get_occurences_of_character(file_content))
main()