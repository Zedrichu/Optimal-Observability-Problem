import gc
from abc import ABC, abstractmethod
from z3 import Context, Solver


class SSPEncoding(ABC):
    def __init__(self):

        self.ctx = None
        self.solver = None

    def reset(self):
        """ Reset for fresh solving context """
        gc.collect() # Clean memory before starting
        self.ctx = Context()
        self.solver = Solver()