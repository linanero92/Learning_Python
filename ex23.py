# edge cases
def is_arguments_for_substr_correct(string, index, substr_length):
    str_end = len(string) - 1
    if substr_length < 0:
        return False
    elif index < 0:
        return False
    elif index > str_end:
        return False
    elif substr_length + index > len(string):
        return False
    else:
        return True

print(is_arguments_for_substr_correct('Sansa Stark', 10, 1))




