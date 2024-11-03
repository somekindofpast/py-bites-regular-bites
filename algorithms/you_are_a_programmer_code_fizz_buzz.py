from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    result = ""
    if num % 3 == 0:
        result = "Fizz"
    if num % 5 == 0:
        result += " Buzz"
    if result != "":
        return result.strip()
    else:
        return num

print(fizzbuzz(5))