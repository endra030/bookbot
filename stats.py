def word_count(content):
    return len(content.split())

def char_count(content):
    character_count = {}
    for c in content:
        #print(f"w: {c}")
        if c.isalpha():
            if c.lower() in character_count:
                character_count[c.lower()] =+ character_count[c.lower()]+1
            else:
                character_count[c.lower()] = 1
        else:
            if c in character_count:
                character_count[c] =+ character_count[c]+1
            else:
                character_count[c] = 1
            character_count[c] =+ character_count[c]+1
        
    return character_count
def sort_on(dict):
    return dict["count"]
def sorted_list_of_char_count_dict(char_count_dict):
    unsorted_char_count_list = []
    for k, v in char_count_dict.items():
        if k.isalpha():
            tmp_dict = {}
            tmp_dict["char"] = k
            tmp_dict["count"] = v
            unsorted_char_count_list.append(tmp_dict)
    unsorted_char_count_list.sort(reverse=True, key=sort_on)
    return unsorted_char_count_list
