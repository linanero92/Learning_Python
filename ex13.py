def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)
