# data aggregation (numbers)
def multiply_numbers_from_range(start, finish):
    i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result

# multiply_numbers_from_range(3, 6)