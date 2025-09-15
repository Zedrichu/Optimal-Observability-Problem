import z3
from z3 import CheckSatResult, ModelRef
from typing import Optional
from dataclasses import dataclass

@dataclass
class ResultTPMC:
    """Results from solving a location tpMC for POMDP instances in OOP"""
    solve_time: float
    # setup_time: float
    # memory_used: int  # bytes
    result: CheckSatResult
    model: Optional[ModelRef] = None
    reward: Optional[z3.ArithRef] = None
    # constraint_count: int = 0
