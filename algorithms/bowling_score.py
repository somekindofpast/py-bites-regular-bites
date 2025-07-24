def calculate_score(frames: str) -> int:
    """Calculates a total 10-pin bowling score from a string of frame data."""
    score = 0
    for i in range(0, len(frames), 2):
        score += _calc_roll_value(frames, i) + _calc_roll_value(frames, i+1)
        if i < 18 and (frames[i] == 'X' or frames[i+1] == '/'):
            score += _calc_roll_value(frames, i+2)
            if frames[i] == 'X':
                score += _calc_roll_value(frames, i+3) if frames[i+2] != 'X' else (_calc_roll_value(frames, i+4) if 5 <= len(frames)-1 - i else _calc_roll_value(frames, i+3))
        elif i+2 == len(frames) - 1:
            score += _calc_roll_value(frames, i+2)
            break
    return score


def _calc_roll_value(frames: str, i: int) -> int:
    if frames[i] == ' ' or frames[i] == '-':
        return 0
    if frames[i] == 'X':
        return 10
    if frames[i] == '/':
        return 10 - _calc_roll_value(frames, i-1)
    return int(frames[i])


if __name__ == '__main__':
    tests = [
                        ('--------------------', 0),
                        ('X X X X X X X X X XXX', 300),
                        ('1-1-1-1-1-1-1-1-1-1-', 10),
                        ('8/9-X X 6/4/X 8-X XXX', 194),
                        ('169-X X 8-41X X 9-53', 140),
                        ('-7188/9-X X X X X XXX', 224),
                        ('36546/819/7--/717/3/-', 117),
                        ('X -/X 5-8/9-X 811-4/X', 137),
                        ('6271X 9-8/X X 35725/8', 140),
                        ('X 9/8/7/6/5/4/3/2/X1/', 165),
                        ('X 7/729/X X X 236/7/3', 168),
                        ('X X X X 9/X X 9/9/XXX', 247),
                        ('8/549-X X 5/53639/9/X', 149),
                        ('X 7/9-X -88/-6X X X81', 167),
                        ('X 9/5/72X X X 9-8/9/X', 187),
                        ('X -/X X X X X X X XXX', 280),
                        ('X 1/X X X X X X X XXX', 280),
                        ('X 2/X X X X X X X XXX', 280),
                        ('X 3/X X X X X X X XXX', 280),
                        ('X 4/X X X X X X X XXX', 280),
                        ('X 5/X X X X X X X XXX', 280),
                        ('X 6/X X X X X X X XXX', 280),
                        ('X 7/X X X X X X X XXX', 280),
                        ('X 8/X X X X X X X XXX', 280),
                        ('X 9/X X X X X X X XXX', 280),
                        ('-/X X X X X X X X XX-', 280),
                        ('1/X X X X X X X X XX-', 280),
                        ('2/X X X X X X X X XX-', 280),
                        ('3/X X X X X X X X XX-', 280),
                        ('4/X X X X X X X X XX-', 280),
                        ('5/X X X X X X X X XX-', 280),
                        ('6/X X X X X X X X XX-', 280),
                        ('7/X X X X X X X X XX-', 280),
                        ('8/X X X X X X X X XX-', 280),
                        ('9/X X X X X X X X XX-', 280),
                        ('X X X X X X X X X X-/', 280),
                        ('X X X X X X X X X X18', 280),
                        ('X X X X X X X X X X26', 280),
                        ('X X X X X X X X X X34', 280),
                        ('X X X X X X X X X X42', 280),
                        ('X X X X X X X X X X5-', 280),
                        ('-/X X X X X X X X XX1', 281),
                        ('1/X X X X X X X X XX1', 281),
                        ('2/X X X X X X X X XX1', 281),
                        ('3/X X X X X X X X XX1', 281),
                        ('4/X X X X X X X X XX1', 281),
                        ('5/X X X X X X X X XX1', 281),
                        ('6/X X X X X X X X XX1', 281),
                        ('7/X X X X X X X X XX1', 281),
                        ('8/X X X X X X X X XX1', 281),
                        ('9/X X X X X X X X XX1', 281),
                        ('X X X X X X X X X X1/', 281),
                        ('X X X X X X X X X X27', 281),
                        ('X X X X X X X X X X35', 281),
                        ('X X X X X X X X X X43', 281),
                        ('X X X X X X X X X X51', 281),
                        ('X X X X X X X X X 54', 263),
                        ('X X X X X X X X 1/54', 245),
                        ('X X X X X X X X -/54', 244),
                        ('X X X X X X X X 54X54', 252),
    ]

    for test in tests:
        print(f"{test[0]}, score: {calculate_score(test[0])}, expected: {test[1]}")