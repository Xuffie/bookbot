# counts the words
def word_counter(words):
    words_counted = len(words.split())

    return words_counted

# counters each char and puts in a dictionary
def letter_counter(words):
    letters = {}

    for char in words:
        lowered = char.lower()
        if lowered not in letters:
            letters[lowered] = 1
        else:
            letters[lowered] += 1

    return letters

# sorts the chars in order of most used to least used
def sort_letters(char_dictionary):
    sorted_list = []
    for char_key in char_dictionary:
        temp_dict = {
            "char": None,
            "num": None
            }
        temp_dict["char"] = char_key
        temp_dict["num"] = char_dictionary[char_key]
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# sort key for .sort()
def sort_on(dict):
    return dict["num"]


