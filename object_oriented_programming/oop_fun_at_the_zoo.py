from collections import defaultdict

BASE_INDEX = 10000

class Animal:
    animal_dict = defaultdict(int)

    def __init__(self, name: str):
        self._name = name.lower()
        if self._name not in Animal.animal_dict:
            Animal.animal_dict[self._name] = BASE_INDEX + len(Animal.animal_dict) + 1

    def __str__(self):
        return f"{Animal.animal_dict[self._name]}. {self._name.title()}"

    @classmethod
    def zoo(cls):
        animal_list = sorted([f"{item[1]}. {item[0].title()}" for item in Animal.animal_dict.items()])
        return '\n'.join(animal_list)


if __name__ == '__main__':
    for animal in 'dog cat fish lion mouse'.split():
        Animal(animal)
    zoo = Animal.zoo()
    expected = ("10001. Dog",
                "10002. Cat",
                "10003. Fish",
                "10004. Lion",
                "10005. Mouse")
    print(zoo)
    assert zoo == '\n'.join(expected)

    horse = Animal('horse')
    print(str(horse))
    assert str(horse) == "10006. Horse"
    monkey = Animal('monkey')
    print(str(monkey))
    assert str(monkey) == "10007. Monkey"