def count_char_occurrences(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def merge_dicts(dict1, dict2, conflict_resolver):
    pass


def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted


def dict_to_table(data_dict, columns):
    pass


def deep_update(base_dict, update_dict):
    pass