import re


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    score = 0
    if re.search(r"[A-Z]+", password) and re.search(r"[a-z]+", password):
        score += 1
    if not password.isdigit() and re.search(r"[0-9]+", password):
        score += 1
    if re.search(r"[@_!#$%^&*()<>?/\\|}{~:]+", password):
        score += 1
    if 8 <= len(password):
        score += 1
        if not re.search(r"(.)\1", password):
            score += 1
    return score