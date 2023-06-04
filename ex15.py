# Python: construction else + if = elif
def who_is_this_house_to_starks(last_name):
    if last_name == 'Karstark' or last_name == 'Tully':
        return 'friend'
    elif last_name == 'Lannister' or last_name == 'Frey':
        return 'enemy'
    else:
        return 'neutral'
print(who_is_this_house_to_starks('Lannister'))
