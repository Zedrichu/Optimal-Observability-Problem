from z3 import CheckSatResult, ModelRef
from typing import Optional
from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    """Results from solving a POMDP instance in OOP (optimal observability problem)"""
    solve_time: float
    # setup_time: float
    # memory_used: int  # bytes
    result: CheckSatResult
    model: Optional[ModelRef] = None
    # constraint_count: int = 0