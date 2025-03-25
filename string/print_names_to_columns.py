from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    for i in range(len(names)):
        print("| " + f"{names[i] : <10}", end='')
        if (i + 1) % cols == 0:
            print('')