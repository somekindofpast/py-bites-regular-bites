import sys
from typing import List, Dict, Tuple


def shortest_path(graph: Dict, start: str, end: str) -> Tuple[int, List]:
    """
       Input: graph: a dictionary of dictionary
              start: starting city   Ex. a
              end:   target city     Ex. b

       Output: tuple of (distance, [path of cites])
       Ex.   (distance, ['a', 'c', 'd', 'b])
    """

    paths: List[Tuple[int, List]] = [(0, [start])]
    while True:
        result = is_path_found(paths, end)
        if result:
            return result

        paths_next: List[Tuple[int, List]] = []
        for path in paths:
            if path[1][-1] == end:
                paths_next.append(path)
                continue
            neighbours: Dict = graph.get(path[1][-1])
            for key in neighbours.keys():
                if key in path[1]:
                    continue
                paths_next.append((path[0] + neighbours[key], path[1][:]))
                paths_next[-1][1].append(key)
        paths = paths_next

def is_path_found(paths: List[Tuple[int, List]], end: str) -> Tuple[int, List] | None:
    min_dist = sys.maxsize
    min_path = []
    for path in paths:
        if path[1][-1] == end:
            if path[0] < min_dist:
                min_dist = path[0]
                min_path = path[1]
        else:
            return None

    return min_dist, min_path

simple = {
          'a': {'b': 2, 'c': 4, 'e': 1},
          'b': {'a': 2, 'd': 3},
          'c': {'a': 4, 'd': 6},
          'd': {'c': 6, 'b': 3, 'e': 2},
          'e': {'a': 1, 'd': 2}
          }

major = {
          'a': {'w': 14, 'x': 7, 'y': 9},
          'b': {'w': 9, 'z': 6},
          'w': {'a': 14, 'b': 9, 'y': 2},
          'x': {'a': 7,  'y': 10, 'z': 15},
          'y': {'a': 9,  'w': 2, 'x': 10, 'z': 11},
          'z': {'b': 6,  'x': 15, 'y': 11},
        }

print(shortest_path(simple, 'a', 'd'))

print(shortest_path(major, 'a', 'b'))