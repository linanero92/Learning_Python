# while loop: reverse
def print_reversed_word_by_symbol(word):
    i = 1
    while i <= len(word):
        print(word[-i])
        i = i + 1


print_reversed_word_by_symbol('cat')