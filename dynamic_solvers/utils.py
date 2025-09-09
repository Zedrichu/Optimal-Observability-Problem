import re
from typing import Tuple, Callable

def parse_threshold(arg: str) -> Tuple[int, int, Callable]:
    sign_idx = arg.find('<')
    if sign_idx == -1:
        raise ValueError("No sign in threshold")
    sign = (lambda x, y: x <= y) if arg[sign_idx + 1] == '=' else (lambda x, y: x < y)
    numerator, denominator = map(int, re.findall(r"\d+", arg))
    return numerator, denominator, sign
