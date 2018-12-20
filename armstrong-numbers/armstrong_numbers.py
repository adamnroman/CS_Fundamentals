def is_armstrong(number):
    num_str = str(number)
    counter = 0
    for digit in num_str:
        counter += int(digit)**len(num_str)
    return counter == number

