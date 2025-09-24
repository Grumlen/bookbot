import sys

from stats import countWords, countCharacters, sortDict

def get_book_text(filePath):
    fileContents = None
    with open(filePath) as file:
        fileContents = file.read()
    return fileContents

def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookContents = get_book_text(sys.argv[1])
    wordCount = countWords(bookContents)
    characterCount = countCharacters(bookContents)
    sortedCount = sortDict(characterCount)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for entry in sortedCount:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
    pass

main()