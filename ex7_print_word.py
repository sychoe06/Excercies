def print_word(word_, multiplier_):
    for i in range(multiplier_):
        print(word_)


# main routine
word = input("Word to print: ")
multiplier = int(input("How many times to print: "))
print_word(word, multiplier)
