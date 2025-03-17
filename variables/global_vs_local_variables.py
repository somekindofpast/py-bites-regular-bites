num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    sum = 0
    for num in numbers:
        sum += num
    global num_hundreds
    num_hundreds += int(sum / 100)
    return sum