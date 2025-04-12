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