def count_words(book_text: str):

    split: list[str] = book_text.split()
    # print(f"The split variable is: {split}")
    num_words: int = len(split)

    return num_words
    # print(f"Found {num_words} total words")


def sort_on(items):
    return items["num"]


def count_characters(book_text: str):

    ### First, get all characters

    
    lower_case: str = book_text.lower()
    
    split_words_list: list = lower_case.split()

    # first_word: str = split_words_list[0]

    dictionary = {}

    # char_count = 0

    for word in split_words_list:
        # print(word)

        for char in word:

            if char not in dictionary:
                ## Initialize char_count
                dictionary[char] = 1

            else:

                dictionary[char] += 1
                
        
            
           # dictionary[char] =+ 1
    
    # print(dictionary)



    list_of_dictionaries = []


    for key, value in dictionary.items():
            new_dict = {
                "char": key, 
                "num": value
            }

            if key.isalpha():
                list_of_dictionaries.append(new_dict)
        
        # print(key, value)

    # print(new_dictionary) 

    # print(list_of_dictionaries)

    return list_of_dictionaries



    # print(dictionary)
    
    # print(f"The number of split_characters is: {split_characters_list}")

def sort_dictionary(list_of_dictionaries):

    # print(list_of_dictionaries)

    sorting_result = sorted(list_of_dictionaries, reverse=True, key=sort_on)

    # print ("---------DEBUG_SORTING_RESULT----------")

    # result_string=""
    
    # for item in sorting_result:
      #  result_string += "\n".join(f"{item['char']}: {item:['num']} for item in sorting_result")

    # print(sorting_result)

    # for item in sorting_result:
        

    return sorting_result

def print_dictionary(sorted_dictionary):

    # print("---FINAL DEBUG---")

    lines = []

    for dictionary in sorted_dictionary:
        charac = dictionary["char"]
        numb = dictionary["num"]
        lines.append(f"{charac}: {numb}")

        
    report_string = "\n".join(lines)

    # print(report_string)
        
    return report_string


    

def print_report(filepath, word_count, report_string):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{report_string}
============= END ===============""")


