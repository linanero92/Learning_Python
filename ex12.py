def word_multiply(text: str, symbol: str, number: int) -> str:
    result: str = (f'{text.replace(symbol, symbol * number)}')
    return result

print(word_multiply('kitten', 'i', 3))