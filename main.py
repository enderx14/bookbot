def main():
  file_path = "books/frankenstein.txt"
  book = get_book_text(file_path)
  print(f"--- Begin report of {file_path} ---")
  print(f"{count_words(book)} words found in the document")
  letters = count_letters(book)
  for letter in letters:
    print(f"The {letter} character was found {letters[letter]} times")
  print("End of report")

def get_book_text(path):
  with open(path)as f:
    return f.read()

def count_words(book):
  return len(book.split())

def count_letters(book):
  chars = []
  dict = {}
  for char in book:
    low_char = char.lower()
    if low_char not in chars and low_char.isalpha():
      chars.append(low_char)
  chars.sort()
  for char in chars:
    count = 0
    for book_char in book:
      if char == book_char.lower():
        count += 1
    dict[char] = count
  return dict

main()
