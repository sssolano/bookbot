def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def number_char(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sorted_dictionarie(dict):
    char_list = []

    def sort_on(dict):
        return dict["count"]

    for char, count in dict.items():
        char_info = {"char": char, "count": count}
        char_list.append(char_info)

    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
