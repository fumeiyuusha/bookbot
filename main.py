def num_of_words(text):
    words = text.split()
    return len(words)

def num_of_characters(text):
    text = text.lower()
    characters = dict()
    for c in text:
        if(c in characters):
            characters[c] += 1
        elif(c.isalpha()):
            characters[c] = 1
    return characters

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = num_of_words(file_contents)
        num_characters = num_of_characters(file_contents)
        print(f"--- Begin report of {f} ---")
        print(f"The book contains {num_words} words\n")
        for record in num_characters:
            print(f"The letter {record} was found {num_characters[record]} times in the document.")
        print("--- End report ---")

main()
