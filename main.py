from stats import (
    chars_dict_to_sorted_list,
    get_chars_dict,
)

import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        path = sys.argv[1]
        text = get_book_text(path)
        chars_dict = get_chars_dict(text)
        chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
        print_report(chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(chars_sorted_list):
    alpha_items = [it for it in chars_sorted_list if it["char"].isalpha()]
    for item in alpha_items[:2]:
        print(f"{item['char']}: {item['num']}")

main()
