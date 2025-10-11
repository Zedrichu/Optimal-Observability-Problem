import re
from typing import Tuple, Callable, List

from z3 import Bool, Real, Context, z3


def parse_threshold(arg: str) -> Tuple[List[int], Callable]:
    sign_idx = arg.find('<')
    if sign_idx == -1:
        raise ValueError("No sign in threshold")
    sign = (lambda x, y: x <= y) if arg[sign_idx + 1] == '=' else (lambda x, y: x < y)

    terms = list(map(int, re.findall(r"\d+", arg)))
    assert len(terms) > 0
    return terms, sign

def init_var_type(condition: bool) -> Callable[[str, Context], z3.ArithRef | z3.BoolRef]:
    """Typed (first-class) constructor selector for Z3 variables based on conditional mode."""
    return Bool if condition else Real
