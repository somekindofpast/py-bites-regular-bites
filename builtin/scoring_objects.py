import builtins
import keyword
import pkgutil
import sys
from typing import Dict, List

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    score = 0
    for obj in objects:
        if obj in list(sys.builtin_module_names) or obj in dir(pkgutil.iter_modules()):
            score += scores["module"]
        elif obj in keyword.kwlist:
            score += scores["keyword"]
        elif obj in dir(builtins):
            score += scores["builtin"]

    return score