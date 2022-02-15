def format_word(word_, num_letters_):
    part1 = word_[0:num_letters_].upper()
    part2 = word_[num_letters_:]
    print(f"{part1}{part2}")


# main routine
word = input("Word to format: ")
num_letters = int(input("How many times to format: "))
format_word(word, num_letters)
