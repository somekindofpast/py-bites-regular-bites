from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...

class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f"{self.name} => {THUMBS_UP * self.value}"

    @classmethod
    def average(cls):
        scores = [score.value for score in Score]
        return sum(scores) / len(scores)

if __name__ == "__main__":
    print(str(Score.ADVANCED))
    print(Score.average())