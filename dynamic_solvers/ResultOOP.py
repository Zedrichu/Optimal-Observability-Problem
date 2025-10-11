from typing import Optional
from dataclasses import dataclass

from z3 import CheckSatResult, ModelRef, ArithRef


@dataclass
class ResultOOP:
    """Results from solving a location tpMC for OOP instances based on Z3 backend."""
    solve_time: float
    # setup_time: float
    # memory_used: int  # bytes
    result: CheckSatResult
    model: Optional[ModelRef] = None
    reward: Optional[ArithRef] = None
    # constraint_count: int = 0
