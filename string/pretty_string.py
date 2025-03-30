import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    return pprint.pformat(obj, width=60, depth=2)