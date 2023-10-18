def main():
    text = open_file_contents("books/frankestein.txt")
    total_words = count_words(text)
    letters = count_letters(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    characters = []
    for letter in letters:
        characters.append(letter)

    characters.sort()
    for character in characters:
        if character.isalpha():
            print(
                f"The '{character}' character was found {letters[character]} times")

    print("--- End report ---")


def open_file_contents(path):
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    chars = {}
    for char in text:
        lower_case = char.lower()
        if lower_case in chars:
            chars[lower_case] += 1
        else:
            chars[lower_case] = 1
    return chars


main()
