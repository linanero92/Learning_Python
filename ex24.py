# syntactic sugar
def filter_string(text, to_delete):
    index = 0
    result = ''
    while index < len(text):
        char = text[index]
        if char == to_delete:
            result
        else:
            result = result + char
        index += 1
    return result


text = 'Python is awesome!'
print(filter_string(text, 'e'))