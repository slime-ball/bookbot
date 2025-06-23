def get_num_words(contents):
    count = len(contents.split())
    return count

def get_num_char(contents):
    lowercase = contents.lower()
    character_counts = {}
    for char in lowercase:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sort_on(items):
    return items["num"]

def sorted_list(contents):
    character_list = []
    for char, count in contents.items():
         if char.isalpha(): 
            char_dict = {"char": char, "num": count}
            character_list.append(char_dict)
    character_list.sort(reverse=True, key=sort_on)
    return character_list
