from stats import word_count
from stats import char_count
from stats import sorted_list_of_char_count_dict
import sys
def get_book_text(file_name):
    file_content = ""
    with open(file_name) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book = sys.argv[1]
    content = get_book_text(book)
    num_words = word_count(content)
    # print(f"{num_words} words found in the document")
    #content = "The Project Gutenberg eBook of Frankenstein; Or, The Modern Prometheus"
    char_count_dict = char_count(content)
    # print(sorted_list_of_char_count_dict(char_count_dict))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_char_count = sorted_list_of_char_count_dict(char_count_dict)
    for d in list_of_char_count:
        # print(f"{d["char"]}:{d["count"]}")
        print(f"{d["char"]}: {d["count"]}")
    print("============= END ===============")




main()
        

