import re
from typing import Tuple, Callable, List

def parse_threshold(arg: str) -> Tuple[List[int], Callable]:
    sign_idx = arg.find('<')
    if sign_idx == -1:
        raise ValueError("No sign in threshold")
    sign = (lambda x, y: x <= y) if arg[sign_idx + 1] == '=' else (lambda x, y: x < y)

    terms = list(map(int, re.findall(r"\d+", arg)))
    assert len(terms) > 0
    return terms, sign
