
# Conditions Inside the Body of the Loop
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string.lower()[index] == char.lower():
            count = count + 1
        index = index + 1
    return count

count_chars('color', 'o')
