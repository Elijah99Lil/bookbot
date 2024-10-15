def character_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(entry):
    return entry["num"]

def count_words(text):
    words = text.split()
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document:")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        count_words(file_contents)
        char_count = character_count(file_contents)
        char_list = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
        char_list.sort(reverse=True, key=sort_on)
        for entry in char_list:
            print(f"The '{entry['char']}' character was found {entry['num']} times")
        print(f"--- End report ---")

if __name__ == "__main__":        
    main()