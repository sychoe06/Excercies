def starts_with_a(word):
    if word[0] == "a":
        return True
    else:
        return False


# main routine
word_to_check = input("Enter word: ")
print(starts_with_a(word_to_check))
