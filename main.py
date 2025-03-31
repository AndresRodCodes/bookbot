import sys
from stats import get_num_words, get_character_counts, sort_dict, print_report

def get_book_text(path):
    file_contents = ''

    with open(path) as f:
        file_contents = f.read()
    
    word_count = get_num_words (file_contents)
    
    character_counts = get_character_counts(file_contents)

    sorted_dict = sort_dict(character_counts)
    print_report(path, word_count, sorted_dict)
    
    return file_contents


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path = sys.argv[1]
    get_book_text(path)

main()