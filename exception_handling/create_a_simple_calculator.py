def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    try:
        op = calculation.split()
        operand_1 = int(op[0])
        operator = op[1]
        operand_2 = int(op[2])
    except:
        raise ValueError

    match operator:
        case "+":
            return operand_1 + operand_2
        case "-":
            return operand_1 - operand_2
        case "*":
            return operand_1 * operand_2
        case "/":
            if operand_2 == 0:
                raise ValueError
            return float(operand_1 / operand_2)
        case _:
            raise ValueError