def character_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def count_words(text):
    words = text.split()
    print(f"There are {len(words)} words lmao. Get hampter'd")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        count_words(file_contents)
        char_count = character_count(file_contents)
        print(char_count)

if __name__ == "__main__":        
    main()