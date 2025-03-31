def get_num_words (string):
    words = string.split()
    return len(words)

def get_character_counts(book_text):
    char_counts = {}
    for char in book_text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def sort_dict(char_counts_dict):
    dict_list = []
    for char, count in char_counts_dict.items():
        dict_list.append({"char": char, "count": count})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_report(path, word_count, char_counts):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for data in char_counts:
        character = data['char']
        char_count = data['count']

        if not character.isalpha():
            continue
        print(f'{character}: {char_count}')
    print('============= END ===============')

    