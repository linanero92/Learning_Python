def get_hidden_card(card_number, count=4):
    hidden = '*' * count
    return (f'{hidden}{card_number[12:16]}')