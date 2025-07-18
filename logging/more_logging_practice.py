import logging
from typing import List  # python 3.9 we can drop this


logger = logging.getLogger('app')


def sum_even_numbers(numbers: List[float]) -> float:
    """
    1. Of the numbers passed in sum the even ones
       and return the result.
    2. If all goes well log an INFO message:
       Input: {numbers} -> output: {ret}
    3. If bad inputs are passed in
       (e.g. one of the numbers is a str), catch
       the exception log it, then reraise it.
    """
    sum_even = 0
    try:
        for num in numbers:
            if isinstance(num, float) or isinstance(num, int):
                if int(num) % 2 == 0:
                    sum_even += num
            else:
                raise TypeError("not all arguments converted during string formatting")
    except:
        logger.exception(f"Bad inputs: {numbers}")
        raise TypeError("not all arguments converted during string formatting")

    logger.info(f"Input: {numbers} -> output: {sum_even}")
    return sum_even