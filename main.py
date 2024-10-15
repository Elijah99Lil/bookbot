def count_words(text):
    words = text.split()
    print(f"There are {len(words)} words lmao. Get hampter'd")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        count_words(file_contents)


if __name__ == "__main__":        
    main()