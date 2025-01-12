from abc import ABC, abstractmethod


class Challenge(ABC):
    def __init__(self, number: int, title: str):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self, to_verify) -> bool:
        pass

    @property
    @abstractmethod
    def pretty_title(self) -> str:
        pass


class BlogChallenge(Challenge):
    def __init__(self, number: int, title: str, merged_prs: list[int]):
        Challenge.__init__(self, number, title)
        self.merged_prs = merged_prs

    def verify(self, to_verify) -> bool:
        return to_verify in self.merged_prs

    @property
    def pretty_title(self) -> str:
        return f"PCC{self.number} - {self.title}"


class BiteChallenge(Challenge):
    def __init__(self, number: int, title: str, result: str):
        Challenge.__init__(self, number, title)
        self.result = result

    def verify(self, to_verify) -> bool:
        return to_verify == self.result

    @property
    def pretty_title(self) -> str:
        return f"Bite {self.number}. {self.title}"