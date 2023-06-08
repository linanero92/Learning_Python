# forming strings in loops
def my_substr(string, length):
    index = 0
    my_substr = ''
    while index < length:
        char = string[index]
        my_substr = my_substr + char
        index = index + 1
    return my_substr

print(my_substr('kitkat', 4))