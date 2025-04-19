import random

names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*sequences):
    for table in zip(*sequences):
        yield SEPARATOR.join(str(x) for x in table)


if __name__ == '__main__':
    print(list(generate_table(names, aliases, points, awake)))