import argparse
import datetime
import sys

def print_hello_world():
    print("Hello, World!")

def reverse_string(string):
    print(string[::-1])

def count_word_frequency(filename):
    word_count = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                word = word.lower()
                if word.isalpha():
                    word_count[word] = word_count.get(word, 0) + 1
    print("Word Frequency:")
    for word, count in sorted(word_count.items()):
        print(f"{word.capitalize()}: {count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Perform various operations based on command-line arguments.")
    parser.add_argument('arg', nargs='?', default=None, help="No argument: prints 'Hello, World!'. String argument: prints the reverse of the string. Text file argument: displays the word frequency.")
    args = parser.parse_args()

    now = datetime.datetime.now()
    print(f"Script executed at: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(sys.argv)
    if args.arg is None:
        print_hello_world()
    elif args.arg.isalpha():
        reverse_string(args.arg)
    else:
        count_word_frequency(args.arg)