def count_words(input_string):
    words = input_string.split()
    return len(words)


def count_characters(input_string):
    chars = {}
    for char in input_string:
        c = char.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def get_sorted_char_list(character_dict):
    char_list = []
    for char, count in character_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list
