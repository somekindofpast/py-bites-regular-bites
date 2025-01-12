SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
RANKS = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(SCORES, RANKS))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score: int) -> str | None:
        """Might be a useful helper"""
        if new_score < SCORES[0]:
            return None
        for i in range(1, len(SCORES)):
            if new_score < SCORES[i]:
                return BELTS[SCORES[i-1]]
        return RANKS[-1]

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError("Score takes an int")
        if new_score <= self._score:
            raise ValueError("Cannot lower score")
        self._score = new_score
        new_belt = self._get_belt(new_score)
        if new_belt != self._last_earned_belt:
            self._last_earned_belt = new_belt
            print(f"Congrats, you earned {new_score} points obtaining the PyBites Ninja {new_belt.title()} Belt")
        else:
            print(f"Set new score to {new_score}")

    score = property(_get_score, _set_score)