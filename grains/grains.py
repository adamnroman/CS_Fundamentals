def on_square(integer_number):
    if integer_number == 1:
        return 1
    elif  2 <= integer_number <= 64:
        return 2 * on_square(integer_number-1)
    else:
        raise ValueError('Chessboards dont have more than 64 squares silly')


def total_after(integer_number):
    if integer_number > 64 or integer_number < 1:
        raise ValueError("1 to 64 pls")
    return 2**integer_number - 1