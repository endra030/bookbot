from stats import word_count
def get_book_text(file_name):
    file_content = ""
    with open(file_name) as f:
        file_content = f.read()
    return file_content


def main():
    content = get_book_text("books/frankenstein.txt")
    num_words = word_count(content)
    print(f"{num_words} words found in the document")

main()
        

